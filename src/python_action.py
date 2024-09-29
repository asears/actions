import sys

def main(filePath, creds):
    print("Hello World")
    print(f"File Path: {filePath}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 myfile.py <filePath> <creds>")
        sys.exit(1)
    filePath = sys.argv[1]
    creds = sys.argv[2]
    main(${{ inputs.directory }}, ${{ inputs.token }})
