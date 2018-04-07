from bson import json_util
import json
from sys import stdout, stderr, stdin, exit
import textwrap

"""File: client/mongoProc.py

This is the client-side version of the mongoProc module.
MongoProc client scripts should import this module.

In EDU-1267 we changed the protocol used by MongoProc scripts
because it didn't support scripts in the .zip bundle format.
However, we continue to support the old protocol for backward compatibility.


Communication from MongoProc client to the client script:
-----------------------------------------------------

The MongoProc client sends configuration data as JSON to the client script on stdin.
Currently this data contains { 'servers': <the servers field from user_settings.json> }.
The servers data is stored in the variable mongoProc.servers when mongoProc is imported.

In the old protocol, client scripts expected 'servers' to be implicitly available as a
global variable, because the MongoProc client would prepend 'servers = { ... data ... }'
to the script. To avoid breaking this expectation, the new protocol prepends the line
'from mongoProc import servers' to all non-zip scripts. New scripts should not
rely on 'servers' being implicitly imported.


Communication from client script to the MongoProc client:
---------------------------------------------------------

Whenever the client script calls mongoProc.addFeedback or
mongoProc.failed, it writes a JSON object to stderr. The JSON is
formatted to be all on one line. This format allows the C++ client to
easily parse the stream of messages, and allows us to easily add new
message types.

When the client script calls mongoProc.complete(), it writes the
state object to stdout.


See server/mongoProc.py for the server-side protocol.

"""

state = {}

def _emit(doc):
    stdout.write(json.dumps(doc, default=json_util.default))
    stdout.write('\n')
    stdout.flush()

def _wrap(string, columns=75):
    """
    Wraps each line in the string, but without merging short lines.
    Also cleans up any indentation or leading and trailing whitespace,
    to make it convenient to pass triple-quoted strings.
    """
    string = textwrap.dedent(string)
    string = string.strip()
    lines = string.split('\n')
    lines = [textwrap.fill(line, columns) for line in lines]
    return '\n'.join(lines)


def addFeedback(summary, detail=''):
    summary = _wrap(summary)
    detail = _wrap(detail)
    _emit({ 'type': 'feedback', 'summary': summary, 'detail': detail })

def failed(message):
    _emit({ 'type': 'failed', 'reason': message })
    exit(1)


def complete():
    _emit({ 'type': 'complete', 'state': state })


try:
    _stdin_json = json.loads(stdin.read())
except:
    failed('Failed to parse JSON data from stdin')

try:
    servers = _stdin_json['servers']
except KeyError as ex:
    failed("Stdin JSON data didn't have a 'servers' field: " + str(_stdin_json))
