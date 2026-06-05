from fastapi import FastAPI, UploadFile, File, Form
import tempfile

from backend.services.screening_services import process_resume
from backend.ai.ranking import rank_candidates
from backend.parser.parser import extract_pdf_text

from backend.database.db import SessionLocal
from backend.database.models import ScreeningResult

app = FastAPI(
title="AI Resume Screening API"
)

@app.get("/")
def home():

    return {
    "status": "running",
    "message": "AI Resume Screening API"
}


@app.post("/screen-resume")
async def screen_resume(
jd_text: str = Form(...),
resume: UploadFile = File(...)
):


    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(
            await resume.read()
        )

        temp_path = temp_file.name

    resume_text = extract_pdf_text(
        temp_path
    )

    result = process_resume(
        jd_text,
        resume_text
    )

    skill_match_score = result[
        "skill_match_score"
    ]

    if skill_match_score >= 80:

        recommendation = (
            "Highly Recommended"
        )

    elif skill_match_score >= 60:

        recommendation = (
            "Recommended"
        )

    else:

        recommendation = (
            "Needs Review"
        )

    db = SessionLocal()

    try:

        new_result = ScreeningResult(

            resume_name=
                resume.filename,

            overall_match_score=
                result[
                    "overall_match_score"
                ],

            skill_match_score=
                skill_match_score,

          
            matched_skills=
                ",".join(
                    result[
                        "matched_skills"
                    ]
                ),

            missing_skills=
                ",".join(
                    result[
                        "missing_skills"
                    ]
                )
        )

        db.add(
            new_result
        )

        db.commit()

    finally:

        db.close()

    result[
        "recommendation"
    ] = recommendation

    return result

@app.post("/screen-multiple-resumes")
async def screen_multiple_resumes(
jd_text: str = Form(...),
resumes: list[UploadFile] = File(...)
):


    results = []

    for resume in resumes:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(
                await resume.read()
            )

            temp_path = temp_file.name

        resume_text = extract_pdf_text(
            temp_path
        )

        result = process_resume(
            jd_text,
            resume_text
        )

        skill_match_score = result[
            "skill_match_score"
        ]

        if skill_match_score >= 80:

            recommendation = (
                "Highly Recommended"
            )

        elif skill_match_score >= 60:

            recommendation = (
                "Recommended"
            )

        else:

            recommendation = (
                "Needs Review"
            )

        
        result[
            "resume_name"
        ] = resume.filename

        results.append(
            result
        )

    ranked_results = rank_candidates(
        results
    )

    for idx, candidate in enumerate(
        ranked_results,
        start=1
    ):

        candidate[
            "rank"
        ] = idx

    return ranked_results


@app.get("/results")
def get_results():

    db = SessionLocal()

    try:

        results = db.query(
            ScreeningResult
        ).all()

        output = []

        for row in results:

            output.append({

                "id": row.id,
                "resume_name": row.resume_name,
                "overall_match_score": row.overall_match_score,
                "skill_match_score": row.skill_match_score,
               
                "matched_skills": row.matched_skills,
                "missing_skills": row.missing_skills

            })

        return output

    finally:

        db.close()