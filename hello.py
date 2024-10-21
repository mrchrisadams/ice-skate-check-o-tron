import rich
import json
import subprocess
from pynotifier import Notification, NotificationClient


def main():
    # import the necesary modeules to run the command below on the command line
    # shot-scraper javascript https://www.eislaufschule.de/kurse/anfaenger-erwachsene.htm -i script.js

    result = subprocess.run(
        [
            "shot-scraper",
            "javascript",
            "https://www.eislaufschule.de/kurse/anfaenger-erwachsene.htm",
            "-i",
            "script.js",
        ],
        capture_output=True,
    )
    output = result.stdout.decode("utf")
    parsed_stdout = json.loads(output)

    available = parsed_stdout.get("available")
    if available:
        rich.print("[green]Available![/green]")
    else:
        rich.print("[red]Not Available![/red]")
        import os

        def send_notification(title, message):
            command = f"""
            osascript -e 'display notification "{message}" with title "{title}"'
            """
            os.system(command)

        # Example usage
        send_notification("Ice skating", "Still not avaiable, will check in an hour")


if __name__ == "__main__":
    main()
