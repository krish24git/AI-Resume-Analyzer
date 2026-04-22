from flask import Blueprint, request, jsonify
from analyzer import analyze_resume
from parse_resume import parse_resume

main = Blueprint("main", __name__)

@main.route("/analyze", methods=["POST"])
def analyze():
    # Get uploaded resume file
    if "resume" not in request.files:
        return jsonify({"error": "No resume file uploaded"}), 400

    file = request.files["resume"]

    # Get job description text
    jd_text = request.form.get("jd", "")
    if not jd_text:
        return jsonify({"error": "No job description provided"}), 400

    # Parse resume text
    resume_text = parse_resume(file)

    # Analyze resume against job description
    score, keywords = analyze_resume(resume_text, jd_text)

    # Return JSON response
    return jsonify({
        "score": score,
        "keywords": list(keywords)
    })
