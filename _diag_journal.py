# DIAGNOSTIC: run on a RECEIVER right after the caller presses share.
# Dumps any journal entry containing the marker, with its author + speech type,
# so we can see whether party chat actually reaches the journal and in what form.

from Assistant import Engine

MARKER = "TARGET"

hits = 0
total = 0
for je in Engine.Journal.GetEntireBuffer():
    if je is None:
        continue
    t = je.Text
    if not t:
        continue
    total += 1
    if MARKER in t:
        hits += 1
        SysMessage("HIT [name=%s type=%s]: %s" % (str(je.Name), str(je.SpeechType), t))

SysMessage("journal entries: %d , FOCUS hits: %d" % (total, hits))
