from aqt import mw
from anki.hooks import addHook
from anki.exporting import AnkiCollectionPackageExporter


def main():
    addHook('unloadProfile', backup)


def backup(*args, **kwargs):
    config = mw.addonManager.getConfig(__name__)
    backup_path = config['backup_path']

    if backup_path is None:
        return

    exporter = AnkiCollectionPackageExporter(mw.col)
    exporter.exportInto(backup_path)


main()
