from aqt import gui_hooks, mw
from anki.exporting import AnkiCollectionPackageExporter


def main() -> None:
    gui_hooks.media_sync_did_start_or_stop.append(backup)


def backup(media_sync_running: bool) -> None:
    if media_sync_running:
        return

    config = mw.addonManager.getConfig(__name__)
    backup_path = config['backup_path']

    if backup_path is None:
        return

    exporter = AnkiCollectionPackageExporter(mw.col)
    exporter.exportInto(backup_path)

    # exportInto closes the collection, so we need to reopen it
    mw.reopen()


main()
