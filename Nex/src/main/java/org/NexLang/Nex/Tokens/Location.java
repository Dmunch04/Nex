package org.NexLang.Nex.Tokens;

public class Location
{

    private int StartLine;
    private int EndLine;
    private int StartColumn;
    private int EndColumn;

    public Location (int StartLine, int EndLine, int StartColumn, int EndColumn)
    {
        this.StartLine = StartLine;
        this.EndLine = EndLine;
        this.StartColumn = StartColumn;
        this.EndColumn = EndColumn;
    }

    public Location None ()
    {
        return new Location (0, 0, 0, 0);
    }

    public Location Copy ()
    {
        return new Location (this.StartLine, this.EndLine, this.StartColumn, this.EndColumn);
    }

}
