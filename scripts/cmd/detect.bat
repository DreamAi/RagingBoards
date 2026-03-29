@echo off
echo Checking system...

where python || echo Python missing
where node || echo Node missing
where docker || echo Docker missing
where git || echo Git missing

echo Done
