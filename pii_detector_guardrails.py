import sys
import json
from guardrails import Guard, OnFailAction
from guardrails.hub import DetectPII

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"processedText": "", "hasPii": False}))
        return

    input_text = sys.argv[1]

    try:
        guard = Guard().use(
            DetectPII,
            on_fail=OnFailAction.NOOP
        )

        raw_output = guard.validate(
            llm_output=input_text
        )

        has_pii = not raw_output.validation_passed

        result = {
            "processedText": input_text,
            "hasPii": has_pii
        }
        print(json.dumps(result))

    except Exception as e:
        print(json.dumps({"processedText": f"Error: {str(e)}", "hasPii": True}))
        sys.exit(1)

if __name__ == "__main__":
    main()