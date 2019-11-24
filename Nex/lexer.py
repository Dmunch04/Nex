from sly import Lexer


class NexLexer (Lexer):
    tokens = {
        MET,
        CLASS,
        BREAK,
        YES,
        NO,
        WHILST,

    }

    literals = {
        "+",
        "-",
        "*",
        "/",
        "%",
        "|",
        "&",
        "!",
        ">",
        "<",
        "=",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
        ";",
        ",",
        ":",
        "[",
        "]",
        "\\",
    }

    ignore = " \t"
    ignore_comment_slash = r"!.*" # comments

    FLOAT = r"\d*\.\d+"
    INT = r"\d+"

    PYTHON_CODE = r"`[.\W\w]*?`"
    STRING = r"(\".*?(?<!\\)(\\\\)*\"|'.*?(?<!\\)(\\\\)*')"
    ID = r"(--[a-zA-Z_]([a-zA-Z0-9_]|!)*--|[a-zA-Z_]([a-zA-Z0-9_]|!)*)"
    # Keywords
    ID["met"] = MET
    ID["class"] = CLASS
    ID["break"] = BREAK
    ID["yes"] = YES
    ID["no"] = NO
    ID["whilst"] = WHILST
    # how are we going to do for loops - what is a synonym for for? as, because, since, being, "as long as", wheras, considering. i like because and since. but they dont really fit do they?
    # lol yeah ok thats fine
    # do you have the syntax of nex like the file we made before. i dont think so. wait yes. but it's on my linux hdd. which i cannot access before i get a new pc :(
    through [myList as item] ( print? [item]. ) # through as in like through this list or through my range. this works better i think. yeah lets keep it then
    ID["through"] = THROUGH
    ID["as"] = AS
    # what about if statements. since or because could work there maybe? just a weird way of saying if lmao -- huh some synonyms for if are: assuming
    expect [bool = yes] ( expr ) # lmao. doubt is a synonym of if. oh yeah. yeah that works. do you wanna just use if here
    else ( expr ) # although assuming and otherwise are too long. hmmmmmmm. and else. create a file called . wait i dont remember the extension oh you mean bnf. i dont remember lmao what its called uhm
    # where are you? lmao was it ebnf lol. yeah ok. making the file
    # lol googling. so i wasnt thinking about bnf, but that works too. no it was something different. but bnf and ebnf works. just so we can declare our syntax fully
    ID["if"] = IF
    ID["else"] = ELSE
    ID["del"] = DEL # tf is this. it was the delete keyword. do we have one? yeah proly. oh. btw class vars and mets will be access with :: maybe? or -> or? i don't know cant we do both. well i guess lmao
    # like do `->` for namespaces and `::`` for class methods. do we have namespaces as well lmao i mean we could probably make them when you import a file but thats it. oh ok. sure
    # ok so `->` for accessing for things inside of modules and `::` for accessing class methods
    # objects->vehicles->carClass[speed:1]::drive[objects->Directions::Forward]. ! This way we have two modules one inside the other. but we should make a new class instance. currently we're calling a function on a class object. that shouldn't be legal. ok ik what you mean i changed ityeah thats works lol. wait should we always instanitiate (idk how to spell) classes?. LOL ik what you mean. hmm. you cant access without doing (java example) new Car (). do you get it? yeah how aout we go python style. yes it was also just an example
    # we need a way to get rid of the namespace cause doing objects->whatever will get annoying. yeah. but how would it know which target namespace? uh in the other file lol we have so many comments here dont delete them tho. other file? what if 2 namespaces has the same variable. then you can't choose. how does python deal with that does it just overwrite i have an idea. in the other file lol
    ID["null"] = NULL # btw do we even want a null type ive heard it can lead to unsaftey. well the lang will not be safe anymore. btw it's staticly typed right? we want it to be right?
    # yeah probably
    ID["return"] = RETURN
    ID["import"] = IMPORT

    COLON_COLON = r"::"
    EQEQ = r"=="
    NOT_EQEQ = r"!="
    EQ_GREATER = r"=>"
    EQ_LESS = r"=<"
    EQ_ADD = r"\+="
    EQ_SUB = r"-="
    EQ_MUL = r"\*="
    EQ_DIV = r"/="
    EQ_MOD = r"%="

    @_(r"\n+")
    def ignore_newline (self, t):
        self.lineno += len (t.value)
