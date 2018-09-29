# Anki backup

Anki add-on to regularly backup your collection to a given path.

A backup is made when you exit Anki, and when you switch user profiles.

You can choose the path to be one that is synchronized with a cloud storage service
e.g. Google Drive.

The full collection, including media, is backed up.


## Configuration

You can configure the path by choosing "Add-ons" from the "Tools" menu,
selecting the add-on and then clicking the "Config" button.

Since the config is in JSON, it is more convenient to use forward slashes in paths in Windows.

For example:

```json
{
    "backup_path": "C:/Users/User Name/Google Drive/anki-collection.colpkg"
}
```
