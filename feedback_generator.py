def generate_feedback(transcript, emotion, filler_count, compound):
    feedback = []
    word_count = len(transcript.split())

    if emotion == "Nervous":
        feedback.append("Try to reduce filler words and speak more confidently.")
    elif emotion == "Neutral":
        feedback.append("You seem composed, but a bit more confidence would help.")

    if filler_count > 4:
        feedback.append("Watch out for filler words like 'um', 'uh', or 'like'.")
    if word_count < 30:
        feedback.append("Try to elaborate more on your answers.")
    if compound >= 0.4:
        feedback.append("Great! Your tone reflects positivity.")
    elif compound <= -0.3:
        feedback.append("Be mindful of sounding too negative during your response.")

    return feedback