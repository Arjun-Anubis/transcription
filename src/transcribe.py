#!/usr/bin/env python3
import argument_parser
import whisper

args = argument_parser.parser.parse_args()
## Print to stderr what file has been selected and what model and ETA

model = whisper.load_model(args.model)
result = model.transcribe(args.file, fp16 = False)

# print(result["text"])
if args.output:
    with open(args.output, "w") as f:
        f.write(result["text"])
else:
    print(result["text"])
