from aqt import gui_hooks, mw
from anki.exporting import AnkiCollectionPackageExporter


def main() -> None:
    gui_hooks.backup_did_complete.append(backup)


def backup() -> None:
    config = mw.addonManager.getConfig(__name__)
    backup_path = config['backup_path']

    if backup_path is None:
        return

    # the collection is closed before the backup_did_complete hook, so reopen it
    mw.reopen()

    exporter = AnkiCollectionPackageExporter(mw.col)
    exporter.exportInto(backup_path)

    # exportInto closes the collection again so we are done



main()
