vragenlijst = [
    {
        "vraag": "Los op: 2^x = 8",
        "antwoord": "x = 3",
        "alternatieven": ["3", "x is 3", "x = log₂(8)"],
        "hint": "2^3 = 8, dus x = 3"
    },
    {
        "vraag": "Bereken log(1000)",
        "antwoord": "3",
        "alternatieven": ["log10(1000)", "x = 3", "x = log(1000) = 3"],
        "hint": "Logaritme met grondtal 10: 10^3 = 1000"
    },
    {
        "vraag": "Herleid: log(a) + log(b)",
        "antwoord": "log(ab)",
        "alternatieven": ["log(a*b)", "log van a maal b", "productregel log"],
        "hint": "Gebruik: log(a) + log(b) = log(ab)"
    },
    {
        "vraag": "Los op: log(x) = log(7)",
        "antwoord": "x = 7",
        "alternatieven": ["7", "x is 7"],
        "hint": "Als log(x) = log(7), dan x = 7"
    },
    {
        "vraag": "Los op: 3^x = 5 met logaritmen",
        "antwoord": "x = log(5) / log(3)",
        "alternatieven": ["x = log₃(5)", "x ≈ 1.464", "log(5)/log(3)"],
        "hint": "Gebruik: x = log(5)/log(3) of x = ln(5)/ln(3)"
    },
    {
        "vraag": "Los op: log(x^2) = 4",
        "antwoord": "x = 100 of x = -100",
        "alternatieven": ["x = ±100", "x = plus of min 100", "x² = 10⁴"],
        "hint": "log(x^2) = 4 → x^2 = 10^4 → x = ±100"
    },
    {
        "vraag": "Los op: ln(x) = 2",
        "antwoord": "x = e^2",
        "alternatieven": ["e²", "x is e²", "x = ongeveer 7.39"],
        "hint": "Neem e-macht aan beide kanten"
    },
    {
        "vraag": "Maak x vrij: y = 3^x",
        "antwoord": "x = log(y) / log(3)",
        "alternatieven": ["x = log₃(y)", "x = ln(y) / ln(3)", "x = logy/log3"],
        "hint": "Neem log aan beide zijden"
    },
    {
        "vraag": "Maak x vrij: y = ln(x + 1)",
        "antwoord": "x = e^y - 1",
        "alternatieven": ["e^y - 1", "x is e^y - 1", "x = e^y minus 1"],
        "hint": "Gebruik de inverse van ln"
    },
    {
        "vraag": "Los op met substitutie: 2^x + 2^(-x) = 5",
        "antwoord": "x = ±ln(2)",
        "alternatieven": ["x = ln(2) of -ln(2)", "plus of min ln(2)", "x = ±0.693"],
        "hint": "Substitueer y = 2^x → y + 1/y = 5 → kwadratische vergelijking"
    },
    {
        "vraag": "Wat is het domein van f(x) = e^x?",
        "antwoord": "Alle reële getallen",
        "alternatieven": ["ℝ", "x ∈ ℝ", "alle x", "R"],
        "hint": "De exponentiële functie is overal gedefinieerd"
    },
    {
        "vraag": "Wat is het bereik van f(x) = e^x?",
        "antwoord": "y > 0",
        "alternatieven": ["(0, ∞)", "alleen positieve y", "y is groter dan 0"],
        "hint": "Exponentiële functies zijn altijd positief"
    },
    {
        "vraag": "Wat is het snijpunt van f(x) = log(x) met de x-as?",
        "antwoord": "x = 1",
        "alternatieven": ["(1, 0)", "snijpunt bij x = 1", "f(1) = 0"],
        "hint": "log(1) = 0"
    },
    {
        "vraag": "Wat is het domein van f(x) = log(x)?",
        "antwoord": "x > 0",
        "alternatieven": ["(0, ∞)", "alleen positieve x", "x is groter dan 0"],
        "hint": "Logaritmen zijn alleen gedefinieerd voor positieve waarden"
    },
    {
        "vraag": "Welke transformatie: f(x) = log(x - 2)?",
        "antwoord": "2 naar rechts",
        "alternatieven": ["horizontale verschuiving 2 naar rechts", "verschuift 2 eenheden naar rechts", "x - 2 = 2 rechts"],
        "hint": "x - 2 betekent verschuiving naar rechts"
    },
    {
        "vraag": "Welke transformatie: f(x) = -log(x)?",
        "antwoord": "Spiegeling in de x-as",
        "alternatieven": ["negatief = x-as spiegeling", "omgekeerd", "spiegelen over x-as"],
        "hint": "Negatief teken voor log → spiegeling in de x-as"
    },
    {
        "vraag": "Je krijgt een rechte lijn op logaritmisch papier. Wat betekent dit?",
        "antwoord": "Exponentieel verband",
        "alternatieven": ["exponentiële groei", "y = a·b^x", "rechte lijn op logpapier = exponentieel"],
        "hint": "Logaritmisch papier lineair → oorsprong was exponentieel"
    },
    {
        "vraag": "Hoe stel je een formule op bij een rechte lijn op logaritmisch papier?",
        "antwoord": "y = a·b^x",
        "alternatieven": ["exponentiële formule", "vorm: y = a·b^x", "y = ab^x"],
        "hint": "Omdat log(y) dan een lineaire relatie heeft met x"
    },
    {
        "vraag": "Wat zegt de verhouding van lijnstukken over exponentiële groei?",
        "antwoord": "Vermenigvuldigen per gelijke stap",
        "alternatieven": ["elke stap vermenigvuldigt", "gelijke verhoudingen", "groei is multiplicatief"],
        "hint": "Exponentiële groei betekent: vermenigvuldigen i.p.v. optellen"
    },
    {
        "vraag": "Wat is het effect van f(x) = log(2x)?",
        "antwoord": "Horizontale compressie",
        "alternatieven": ["sneller stijgen", "horizontale vermenigvuldiging met 1/2", "log wordt steiler"],
        "hint": "log(2x) betekent horizontaal in elkaar gedrukt"
    },
{
        "vraag": "Wat is de groeifactor bij een toename van 5% per stap?",
        "antwoord": "1.05",
        "alternatieven": ["1,05", "g = 1.05", "groeifactor = 1.05"],
        "hint": "Groeifactor = 1 + groeipercentage/100"
    },
    {
        "vraag": "Wat is de groeifactor bij een afname van 8%?",
        "antwoord": "0.92",
        "alternatieven": ["0,92", "g = 0.92", "groeifactor = 0.92"],
        "hint": "Groeifactor = 1 - afnamepercentage/100"
    },
    {
        "vraag": "Hoe bereken je het groeipercentage bij groeifactor 1.2?",
        "antwoord": "20%",
        "alternatieven": ["+20%", "groei is 20%", "1.2 = +20%"],
        "hint": "g = 1 + p → p = (g - 1) × 100%"
    },
    {
        "vraag": "Wat is de formulevorm bij exponentiële groei?",
        "antwoord": "N(t) = N₀ · g^t",
        "alternatieven": ["N = N₀ · g^t", "begingetal · groeifactor^tijd", "exponentiële groeiformule"],
        "hint": "Exponentiële formules hebben de vorm N = N₀ · g^t"
    },
    {
        "vraag": "Wat is de verdubbelingstijd bij groeifactor 2?",
        "antwoord": "1",
        "alternatieven": ["1 tijdseenheid", "één", "t = 1"],
        "hint": "Als g = 2, dan verdubbelt het per stap"
    },
    {
        "vraag": "Hoe bereken je de verdubbelingstijd bij g = 1.05?",
        "antwoord": "t = log(2)/log(1.05)",
        "alternatieven": ["log(2)/log(1.05)", "≈ 14.21", "t ≈ 14.2"],
        "hint": "Gebruik: 2 = 1.05^t → neem log aan beide zijden"
    },
    {
        "vraag": "Wat is de halveringstijd bij groeifactor 0.5?",
        "antwoord": "1",
        "alternatieven": ["1 tijdseenheid", "t = 1", "één"],
        "hint": "Bij 0.5 halveert het elke stap"
    },
    {
        "vraag": "Hoe bereken je de halveringstijd bij g = 0.9?",
        "antwoord": "t = log(0.5)/log(0.9)",
        "alternatieven": ["log(0.5)/log(0.9)", "≈ 6.58", "t ≈ 6.6"],
        "hint": "Gebruik: 0.5 = 0.9^t → neem log aan beide zijden"
    },
    {
        "vraag": "Hoe weet je of er sprake is van exponentiële groei of afname?",
        "antwoord": "Groeifactor groter of kleiner dan 1",
        "alternatieven": ["g > 1 is groei, g < 1 is afname", "afleiden uit g", "groeifactor bepaalt type"],
        "hint": "g > 1 = groei, g < 1 = afname"
    },
    {
        "vraag": "Wat gebeurt er met de waarde bij g = 1?",
        "antwoord": "Blijft constant",
        "alternatieven": ["geen groei", "waarde blijft gelijk", "constante functie"],
        "hint": "Groeifactor 1 = geen verandering per stap"
    }
]
