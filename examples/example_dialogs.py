import sys
sys.path.append(".")

from pathlib import Path

from aq3d_api.containers.dialogs import Dialogs


def get_dialogs(min_index: int = 1, max_index: int = 1):
    # Creates a Dialogs instance which creates a bundle of dialogs based on
    # the min and max index ranges.
    return Dialogs({
        "min-index": min_index,
        "max-index": max_index
    })


if __name__ == "__main__":
    # Create a Dialogs object with dialog IDs between 1 and 20.
    dialogs = get_dialogs(1, 20)
    # Update the dialogs container at least once to gather the API data.
    dialogs.update()

    # Save dialogs to either a CSV file or JSON file.
    dialogs.to_csv(Path("./dialogs.csv"))
    dialogs.to_json_file(Path("./dialogs.json"))

    # Get all the frames within a dialog, which is basically each
    # frame of a dialog with its own speaker, title of speaker and text.
    dialog_frames = dialogs[0].frames
    print(dialog_frames)
