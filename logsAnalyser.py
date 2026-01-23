import argparse
import sys

def checkLogType(line_parts, stats): # dictionary, that holds the different types of logs
    """Updates the stats dictionary based on the log level."""
    if len(line_parts) < 3:
        return

    log_level = line_parts[2]
    
    if log_level == 'ERROR':
        stats['errors'] += 1
        stats['errorLogs'].append(line_parts)
    elif log_level == 'WARN':
        stats['warns'] += 1
        stats['warnLogs'].append(line_parts)

def main():
    parser = argparse.ArgumentParser(description="Analyze log files for Errors and Warnings.")
    
    parser.add_argument("filename", help="The path to the log file you want to analyze")
    
    parser.add_argument("-v", "--verbose", action="store_true", help="Show the content of the error/warn logs")

    args = parser.parse_args()

    # Data structure to hold our results (replaces global variables)
    stats = {
        'errors': 0,
        'errorLogs': [],
        'warns': 0,
        'warnLogs': []
    }


    try:
        # 3. Use the filename provided in the command line
        with open(args.filename, 'r') as f:
            for line in f:
                words = line.split()
                checkLogType(words, stats)

        # 4. Output results
        print(f"--- Analysis for {args.filename} ---")
        print(f"Found {stats['errors']} errors")
        print(f"Found {stats['warns']} warnings")

        # Use the flag logic
        if args.verbose:
            print("\nError Logs:")
            for log in stats['errorLogs']:
                print(" ".join(log))
            print("\nWarning Logs:")
            for log in stats['warnLogs']:
                print("".join(log))

    except FileNotFoundError:
        print(f"Error: The file '{args.filename}' was not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()