import sys
import json
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"processedText": "", "hasPii": False}))
        return

    input_text = sys.argv[1]

    try:
        analyzer = AnalyzerEngine()
        
        anonymizer = AnonymizerEngine()

        results = analyzer.analyze(
            text=input_text,
            entities=[
                "PERSON",
                "EMAIL_ADDRESS",
                "PHONE_NUMBER",
                "LOCATION",
                "DATE_TIME",
                "URL",
                "AU_TFN",
                "AU_ABN",
                "AU_ACN",
                "AU_MEDICARE"
            ],
            language='en'
        )

        anonymized_text = anonymizer.anonymize(
            text=input_text,
            analyzer_results=results,
            operators={
                "PERSON": OperatorConfig("replace", {"new_value": "<NAME>"}),
                "EMAIL_ADDRESS": OperatorConfig("replace", {"new_value": "<EMAIL>"}),
                "PHONE_NUMBER": OperatorConfig("replace", {"new_value": "<PHONE>"}),
                "LOCATION": OperatorConfig("replace", {"new_value": "<ADDRESS>"}),
                "AU_TFN": OperatorConfig("replace", {"new_value": "<TFN>"}),
                "DEFAULT": OperatorConfig("replace", {"new_value": "<PII>"})
            }
        ).text

        has_pii = anonymized_text != input_text

        result = {
            "processedText": anonymized_text,
            "hasPii": has_pii
        }
        print(json.dumps(result))

    except Exception as e:
        print(json.dumps({"processedText": f"Error: {str(e)}", "hasPii": True}))
        sys.exit(1)

if __name__ == "__main__":
    main()