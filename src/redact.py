from PIL import Image
from presidio_image_redactor import ImageRedactorEngine
from presidio_analyzer import AnalyzerEngine, RecognizerResult
from presidio_analyzer.predefined_recognizers import SpacyRecognizer
from transformers import pipeline

analyzer = AnalyzerEngine()

spacy_recognizer = SpacyRecognizer()
analyzer.registry.add_recognizer(spacy_recognizer)

def redact_image(image_path: str):
    redactor = ImageRedactorEngine(image_analyzer_engine= analyzer)
    image = Image.open(image_path)
    return redactor.redact(
        image=image,
        analyzer_results=analyzer_results
    )

# def analyze_text(text: str):
#     results: list[RecognizerResult] = analyzer.analyze(
#         text=text,
#         language="en"
#     )
#     return results
