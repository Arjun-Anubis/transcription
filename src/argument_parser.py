import argparse as ap

## Our first program is called transcribe
prog = "transcribe"
description = """
This program transcribes mp3 files into text using the whisper service from openAI, it also also extracts some metadata concerning the tone and mood of the speaker. It can handle background noise, variation in tone and pace and multiple speakers. The model size can be configured using the options.
"""
epilogue = """
This program is a part of a set of programs used for the IITD Rendezvous hackathon
"""

parser = ap.ArgumentParser(
    prog = prog,
    description = description,
    epilog = epilogue
)

parser.add_argument("file", 
                    help="The mp3 file to transcribe" )
parser.add_argument("-m", "--model", 
                    help="Choose the model to user, tiny, base, turbo" )

parser.add_argument("-v", "--verbose", 
                    action="store_true", 
                    help="Verbose output" )

parser.add_argument("-o", "--output", 
                    help="Choose an output file" )

if __name__ == "__main__":
    args = parser.parse_args()
