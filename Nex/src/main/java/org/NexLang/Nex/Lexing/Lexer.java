package org.NexLang.Nex.Lexing;

import org.NexLang.Nex.Tokens.Token;

import java.util.List;

public class Lexer
{

    private String Read;
    private List<Token> Tokens;
    private static int Index = 0;

    public Lexer (String Read, List<Token> Tokens)
    {
        this.Read = Read;
        this.Tokens = Tokens;
    }

    public void Lex ()
    {

    }

    private char Peek ()
    {
        return Read.charAt (Index + 1);
    }

    private char Peek (int Amount)
    {
        return Read.charAt (Index + Amount);
    }

    public String GetRead () { return Read; }
    public List<Token> GetTokens () { return Tokens; }

}
