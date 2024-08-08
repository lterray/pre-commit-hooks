import sys
import subprocess
import re


def main():
    current_branch_command = "git rev-parse --abbrev-ref HEAD 2>/dev/null"
    result = subprocess.run(current_branch_command, capture_output=True, text=True, shell=True)
    current_branch = result.stdout.strip()
    print(f'current_branch: {current_branch}')

    if current_branch:
        numeric_values = re.findall(r'[0-9]+', current_branch)
        print(f'numeric_values: {numeric_values}')

        if len(numeric_values):
            ticket_id = numeric_values[0]
            print(f'ticket_id: {ticket_id}')

            # Path to the commit message file
            print(f'sys.argv: {sys.argv}')
            commit_msg_filepath = sys.argv[1]

            with open(commit_msg_filepath, 'r+') as f:
                print(f'commit_msg_filepath: {commit_msg_filepath}')

                content = f.read()
                f.seek(0, 0)
                f.write(str(ticket_id) + ' ' + content)

    return 0

if __name__ == '__main__':
    sys.exit(main())