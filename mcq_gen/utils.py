import os
import json
import pandas as pd
import traceback
import PyPDF2


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PDFFileReader(file)
            text=""
            for page in pdf_reader.pages:
                text+=page.extract_text()
            return text

        except Exception as e:
            raise Exception("error reading the PDF file")

    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception(
            "Unsupported file format !! Only PDF and text file supported."
        )

def get_table_data(quiz_str):
    try:
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        for key,value in quiz_dict.items():
            mcq = value["mcq"]
            options= " || ".join(
                [
                    f"{option}->{option_value}" for option, option_value in value["options"].items()
                ]
            )

            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})

        return quiz_table_data

    except Exception as e:
        traceback.print_exception(type(e), e, e.traceback_)
        return False