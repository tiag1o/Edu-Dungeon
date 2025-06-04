vragenlijst = [
    {
        "vraag": "Differentieer: f(x) = x^2 + 3x",
        "antwoord": "2x + 3",
        "hint": "Pas de somregel toe: differentieer beide termen apart"
    },
    {
        "vraag": "Differentieer: f(x) = x^3 * x^2",
        "antwoord": "5x^4",
        "hint": "Herschrijf eerst als x^5 en differentieer dan met de machtsregel"
    },
    {
        "vraag": "Differentieer: f(x) = (x^2 + 1)(x - 3)",
        "antwoord": "2x(x - 3) + (x^2 + 1)",
        "hint": "Gebruik de productregel: f' = u'v + uv'"
    },
    {
        "vraag": "Differentieer: f(x) = (3x + 1)/(x^2)",
        "antwoord": "(3x^2 - 6x - 1)/x^4",
        "hint": "Gebruik de quotiëntregel: f' = (u'v - uv') / v^2"
    },
    {
        "vraag": "Differentieer: f(x) = (x^2 + 2)/(x + 1)",
        "antwoord": "((2x)(x + 1) - (x^2 + 2)(1)) / (x + 1)^2",
        "hint": "Gebruik de quotiëntregel: f' = (u'v - uv') / v^2"
    },
    {
        "vraag": "Differentieer: f(x) = sin(3x)",
        "antwoord": "3cos(3x)",
        "hint": "Kettingregel: buitenste afgeleide is cos(3x), binnenste is 3"
    },
    {
        "vraag": "Differentieer: f(x) = (x^2 + 1)^3",
        "antwoord": "6x(x^2 + 1)^2",
        "hint": "Gebruik de kettingregel: afgeleide van buiten × afgeleide van binnen"
    },
    {
        "vraag": "Differentieer: f(x) = √(4x + 1)",
        "antwoord": "2 / √(4x + 1)",
        "hint": "Gebruik de kettingregel: herschrijf eerst als (4x + 1)^(1/2)"
    },
    {
        "vraag": "Differentieer: f(x) = ln(2x + 1)",
        "antwoord": "2 / (2x + 1)",
        "hint": "Kettingregel: afgeleide van ln(u) is 1/u × u'"
    },
    {
        "vraag": "Differentieer: f(x) = e^(x^2)",
        "antwoord": "2x * e^(x^2)",
        "hint": "Gebruik de kettingregel: afgeleide van e^u is e^u × u'"
    },
    {
        "vraag": "Bepaal de extreme waarden van f(x) = x^2 - 4x + 3",
        "antwoord": "Minimum bij x = 2, f(2) = -1",
        "alternatieven": ["minimum bij x = 2", "x = 2, f(2) = -1", "min bij x = 2", "x = 2"],
        "hint": "Stel f'(x) = 0 en los op: f'(x) = 2x - 4 → x = 2"
    },
    {
        "vraag": "Bepaal de extreme waarden van f(x) = -x^2 + 6x",
        "antwoord": "Maximum bij x = 3, f(3) = 9",
        "alternatieven": ["maximum bij x = 3", "x = 3, f(3) = 9", "max bij x = 3", "x = 3"],
        "hint": "f'(x) = -2x + 6, stel gelijk aan 0 en bereken f(x)"
    },
    {
        "vraag": "Toon aan dat f(x) = x^3 - 3x stijgt, daalt en weer stijgt",
        "antwoord": "f'(x) = 3x^2 - 3: positief bij x < -1 en x > 1, negatief tussenin",
        "alternatieven": ["stijgt voor x < -1 en x > 1", "daalt tussen x = -1 en x = 1", "stijgt, daalt, stijgt", "wisselt stijging"],
        "hint": "Onderzoek het teken van f'(x) = 3x^2 - 3"
    },
    {
        "vraag": "Bepaal het buigpunt van f(x) = x^3 - 3x",
        "antwoord": "Buigpunt bij x = 0, f(0) = 0",
        "alternatieven": ["x = 0", "buigpunt x = 0", "f''(x) = 6x, dus x = 0"],
        "hint": "Zoek waar f''(x) = 0: f''(x) = 6x → x = 0"
    },
    {
        "vraag": "Bepaal het buigpunt van f(x) = x^4",
        "antwoord": "Geen buigpunt, want f''(x) = 12x^2 is nooit negatief",
        "alternatieven": ["geen buigpunt", "altijd positief", "nooit tekenwisseling"],
        "hint": "Buigpunten ontstaan waar f''(x) wisselt van teken"
    },
    {
        "vraag": "Stel de raaklijn op aan f(x) = x^2 bij x = 1",
        "antwoord": "y = 2x - 1",
        "alternatieven": ["2x - 1", "raaklijn: y = 2x - 1", "y = 2(x - 1) + 1"],
        "hint": "Gebruik: y = f'(a)(x - a) + f(a); hier f'(1) = 2, f(1) = 1"
    },
    {
        "vraag": "Stel de raaklijn op aan f(x) = √x bij x = 4",
        "antwoord": "y = (1/4)x + 1",
        "alternatieven": ["0.25x + 1", "raaklijn: y = (1/4)x + 1", "y = 0.25x + 1"],
        "hint": "f(4) = 2, f'(x) = 1/(2√x) → f'(4) = 1/4, gebruik raaklijnformule"
    },
    {
        "vraag": "Stel de raaklijn op aan f(x) = ln(x) bij x = 1",
        "antwoord": "y = x - 1",
        "alternatieven": ["x - 1", "raaklijn: y = x - 1", "y = 1(x - 1) + 0"],
        "hint": "f(1) = 0, f'(1) = 1 → raaklijn: y = 1(x - 1) + 0"
    },
    {
        "vraag": "Bepaal de parameter a waarvoor de grafiek van f(x) = ax^2 + 2x een minimum heeft bij x = -1",
        "antwoord": "a = 1",
        "alternatieven": ["1", "a is 1", "waarde van a is 1"],
        "hint": "Minimum ligt waar f'(x) = 0 → f'(x) = 2ax + 2 = 0 → x = -1 geeft a = 1"
    },
    {
        "vraag": "Bepaal de raaklijn aan f(x) = ax^2 bij x = 2 als de helling daar 8 moet zijn",
        "antwoord": "a = 2",
        "alternatieven": ["2", "a is 2", "waarde van a is 2"],
        "hint": "f'(x) = 2ax, stel 2a(2) = 8 → a = 2"
    },
    {
        "vraag": "Wat is een primitieve van f(x) = 2x?",
        "antwoord": "x^2 + C",
        "alternatieven": ["x^2", "x^2 + c", "x² + C", "x² + c"],
        "hint": "Zoek een functie waarvan de afgeleide 2x is"
    },
    {
        "vraag": "Wat is een primitieve van f(x) = x^3?",
        "antwoord": "1/4 x^4 + C",
        "alternatieven": ["x^4/4 + C", "x^4/4 + c", "¼x^4 + C"],
        "hint": "Verhoog de exponent en deel door de nieuwe macht"
    },
    {
        "vraag": "Primitieve van f(x) = √x?",
        "antwoord": "2/3 x^(3/2) + C",
        "alternatieven": ["(2/3)x^(3/2) + C", "2x^(3/2)/3 + C", "2x^1.5/3 + C"],
        "hint": "Herschrijf √x als x^(1/2) en pas machtsregel toe"
    },
    {
        "vraag": "Primitieve van f(x) = e^x?",
        "antwoord": "e^x + C",
        "alternatieven": ["e^x", "e^x + c"],
        "hint": "De afgeleide en primitieve van e^x zijn gelijk"
    },
    {
        "vraag": "Primitieve van f(x) = 1/x?",
        "antwoord": "ln|x| + C",
        "alternatieven": ["ln(x) + C", "ln|x|", "ln(x)"],
        "hint": "De afgeleide van ln|x| is 1/x"
    },
    {
        "vraag": "Primitieve van f(x) = sin(x)?",
        "antwoord": "-cos(x) + C",
        "alternatieven": ["-cos(x)", "-cos(x) + c"],
        "hint": "De afgeleide van -cos(x) is sin(x)"
    },
    {
        "vraag": "Primitieve van f(x) = cos(x)?",
        "antwoord": "sin(x) + C",
        "alternatieven": ["sin(x)", "sin(x) + c"],
        "hint": "De afgeleide van sin(x) is cos(x)"
    },
    {
        "vraag": "Primitieve van f(x) = 1 / (x + 1)?",
        "antwoord": "ln|x + 1| + C",
        "alternatieven": ["ln(x + 1) + C", "ln|x + 1|", "ln(x + 1)"],
        "hint": "Kijk naar de standaardvorm ∫1/u du = ln|u| + C"
    },
    {
        "vraag": "Primitieve van f(x) = 2x * cos(x^2)?",
        "antwoord": "sin(x^2) + C",
        "alternatieven": ["sin(x²) + C", "sin(x^2)", "sin(x²)"],
        "hint": "Kettingregel omgekeerd: afgeleide van binnen is 2x"
    },
    {
        "vraag": "Toon aan dat F(x) = 1/3 x^3 + 2x + 5 een primitieve is van f(x) = x^2 + 2",
        "antwoord": "F'(x) = x^2 + 2",
        "alternatieven": ["de afgeleide is x^2 + 2", "F' = x^2 + 2", "afgeleide klopt"],
        "hint": "Differentieer F(x) om te controleren of je f(x) terugkrijgt"
    },
    {
        "vraag": "Hoe bereken je de oppervlakte onder de grafiek van f(x) op [a, b]?",
        "antwoord": "Door ∫ₐᵇ f(x) dx te berekenen",
        "alternatieven": ["integraal van f van a tot b", "∫ van f(x) tussen a en b", "oppervlakte = integraal"],
        "hint": "Oppervlakte = bepaalde integraal van f(x)"
    },
    {
        "vraag": "Hoe bepaal je de oppervlakte onder f(x) = ax op [0, 2]?",
        "antwoord": "a * 2^2 / 2 = 2a",
        "alternatieven": ["2a", "a * 2", "oppervlakte = 2a"],
        "hint": "Gebruik: ∫₀² ax dx = a ∫₀² x dx = a * (1/2 * x^2)"
    },
    {
        "vraag": "Hoe bepaal je de oppervlakte tussen f(x) = x^2 en g(x) = x op [0, 1]?",
        "antwoord": "∫₀¹ (x - x^2) dx = 1/6",
        "alternatieven": ["1/6", "≈ 0.1667", "integraal van verschil"],
        "hint": "Bereken ∫ (bovenste - onderste)"
    },
    {
        "vraag": "Hoe bereken je de inhoud van een lichaam door wenteling om de x-as?",
        "antwoord": "π ∫ₐᵇ [f(x)]² dx",
        "alternatieven": ["π * integraal van f(x)^2", "π∫f(x)^2dx", "pi keer kwadraat integraal"],
        "hint": "Gebruik schijvensmethode: πr²dx"
    },
    {
        "vraag": "Hoe bereken je de inhoud tussen twee functies bij wenteling om de x-as?",
        "antwoord": "π ∫ₐᵇ ([f(x)]² - [g(x)]²) dx",
        "alternatieven": ["pi keer verschil van kwadraten", "π∫(f^2 - g^2)dx", "inhoud tussen grafieken"],
        "hint": "Gebruik: π(r_boven² - r_onder²)"
    },
    {
        "vraag": "Hoe wentel je f(x) om de y-as?",
        "antwoord": "Gebruik x = g(y) en π ∫ [g(y)]² dy",
        "alternatieven": ["integraal over y", "wissel van x naar y", "π∫g(y)^2 dy"],
        "hint": "Herformuleer functie in y en pas schijvensmethode toe"
    },
    {
        "vraag": "Hoe bereken je de booglengte van f(x)?",
        "antwoord": "∫ₐᵇ √(1 + [f'(x)]²) dx",
        "alternatieven": ["wortelregel", "booglengteformule", "∫ √(1 + f'²)"],
        "hint": "Gebruik formule met de afgeleide onder een wortel"
    },
    {
        "vraag": "Wat is de inhoud van een bolschijf met straal r?",
        "antwoord": "πr²dx",
        "alternatieven": ["pi r kwadraat dx", "π * r^2 * dx"],
        "hint": "Standaardformule: inhoud van een dun schijfje"
    },
    {
        "vraag": "Wat is een kegelsnede bij wenteling?",
        "antwoord": "Inhoud tussen rechte lijn en x-as om x-as",
        "alternatieven": ["schuine lijn om x-as", "draai een driehoek om", "vorm: kegel"],
        "hint": "Bijv. f(x) = x op [0, h] → kegelvorm"
    },
    {
        "vraag": "Wat betekent een verhouding van oppervlakten?",
        "antwoord": "Vergelijking tussen twee integralen",
        "alternatieven": ["oppervlakte A / oppervlakte B", "verhouding integralen", "deel / geheel"],
        "hint": "Bijv. ∫f(x) dx gedeeld door ∫g(x) dx"
    }
]
