vragenlijst = [
    {
        "vraag": "Zet om naar radialen: 180°",
        "antwoord": "π",
        "alternatieven": ["π radialen", "pi", "pi rad"],
        "hint": "180° = π radialen. Dit is de basisomrekening."
    },
    {
        "vraag": "Zet om naar graden: π/2",
        "antwoord": "90°",
        "alternatieven": ["90", "90 graden", "π/2 = 90°"],
        "hint": "π/2 × (180/π) = 90°"
    },
    {
        "vraag": "Wat is sin(π)?",
        "antwoord": "0",
        "alternatieven": ["nul", "0.0", "sin(π) = 0"],
        "hint": "Gebruik de eenheidscirkel: op π zit het punt (-1, 0)"
    },
    {
        "vraag": "Wat is cos(0)?",
        "antwoord": "1",
        "alternatieven": ["cos(0) = 1", "één", "1.0"],
        "hint": "Beginpunt op de eenheidscirkel: (1, 0)"
    },
    {
        "vraag": "Los op: sin(x) = 0",
        "antwoord": "x = 0, π, 2π, ...",
        "alternatieven": ["x = nπ", "x = 0 + nπ", "veelvouden van π"],
        "hint": "Sinus is nul op de x-as: 0, π, 2π, ..."
    },
    {
        "vraag": "Los op: cos(x) = -1",
        "antwoord": "x = π + 2nπ",
        "alternatieven": ["x = π", "π + n·2π", "x = π, 3π, 5π, ..."],
        "hint": "Cosinus is -1 bij x = π (180°)"
    },
    {
        "vraag": "Los op: sin(x) = 1/2",
        "antwoord": "x = π/6 + 2nπ en x = 5π/6 + 2nπ",
        "alternatieven": ["π/6 en 5π/6", "hoeken in Q1 en Q2", "x = π/6 ± n·2π en 5π/6 ± n·2π"],
        "hint": "Sinus is positief in kwadrant I en II"
    },
    {
        "vraag": "Los op: cos(x) = √3/2",
        "antwoord": "x = π/6 + 2nπ en x = 11π/6 + 2nπ",
        "alternatieven": ["π/6 en 11π/6", "kwadrant I en IV", "hoeken met cos = √3/2"],
        "hint": "Cos is positief in kwadrant I en IV"
    },
    {
        "vraag": "Los op: sin(x) = sin(π/3)",
        "antwoord": "x = π/3 + 2nπ of x = 2π/3 + 2nπ",
        "alternatieven": ["x = π/3 en 2π/3", "hoeken met gelijke sinus", "spiegels in eenheidscirkel"],
        "hint": "Gebruik: sin(x) = sin(a) → x = a + 2nπ of π - a + 2nπ"
    },
    {
        "vraag": "Los op: cos(x) = cos(2π/3)",
        "antwoord": "x = 2π/3 + 2nπ of x = 4π/3 + 2nπ",
        "alternatieven": ["2π/3 en 4π/3", "symmetrie rond x-as", "cos(a) = cos(-a + 2π)"],
        "hint": "Cos(x) = cos(a) → x = a ± 2nπ en -a ± 2nπ"
    },
    {
        "vraag": "Los op: tan(x) = 1",
        "antwoord": "x = π/4 + nπ",
        "alternatieven": ["π/4", "x = π/4 + nπ", "45° + 180°"],
        "hint": "Tangens is periodiek met π"
    },
    {
        "vraag": "Los op: tan(x) = 0",
        "antwoord": "x = nπ",
        "alternatieven": ["x = 0, π, 2π, ...", "veelvouden van π", "x = 0 + nπ"],
        "hint": "Tangens is nul als sin(x) = 0"
    },
    {
        "vraag": "Los op: sin(2x) = 0",
        "antwoord": "x = 0, π/2, π, ...",
        "alternatieven": ["x = nπ/2", "veelvouden van π/2", "x = 0 + nπ/2"],
        "hint": "Gebruik eerst de dubbele hoekregel: sin(2x) = 0"
    },
    
    {
        "vraag": "Herleid: sin^2(x) + cos^2(x)",
        "antwoord": "1",
        "alternatieven": ["= 1", "altijd 1", "fundamentele identiteit"],
        "hint": "Basisidentiteit: sin²(x) + cos²(x) = 1"
    },
    {
        "vraag": "Herleid: 1 + tan^2(x)",
        "antwoord": "1 / cos^2(x)",
        "alternatieven": ["sec²(x)", "1/cos²(x)", "herken identiteit tan"],
        "hint": "Gebruik: 1 + tan²(x) = 1/cos²(x)"
    },
    {
        "vraag": "Herleid: 2sin(x)cos(x)",
        "antwoord": "sin(2x)",
        "alternatieven": ["= sin(2x)", "dubbele hoekformule", "2sin·cos = sin dubbelhoek"],
        "hint": "Gebruik verdubbelingsformule: sin(2x) = 2sin(x)cos(x)"
    },
    {
        "vraag": "Herleid: cos^2(x) - sin^2(x)",
        "antwoord": "cos(2x)",
        "alternatieven": ["= cos(2x)", "dubbele hoek cos", "cos² - sin² = cos dubbelhoek"],
        "hint": "cos(2x) = cos²(x) - sin²(x)"
    },
    {
        "vraag": "Herleid: sin(a + b)",
        "antwoord": "sin(a)cos(b) + cos(a)sin(b)",
        "alternatieven": ["sin·cos + cos·sin", "somformule sinus", "sin(a)cos(b) + cos(a)sin(b)"],
        "hint": "Gebruik somformule voor sin(a + b)"
    },
    {
        "vraag": "Herleid: cos(a + b)",
        "antwoord": "cos(a)cos(b) - sin(a)sin(b)",
        "alternatieven": ["cos·cos - sin·sin", "somformule cosinus", "cos(a + b) = cos(a)cos(b) - sin(a)sin(b)"],
        "hint": "Gebruik somformule voor cos(a + b)"
    },
    {
        "vraag": "Herleid: sin(a - b)",
        "antwoord": "sin(a)cos(b) - cos(a)sin(b)",
        "alternatieven": ["sin·cos - cos·sin", "sin(a - b) = sin(a)cos(b) - cos(a)sin(b)"],
        "hint": "Gebruik verschilformule voor sinus"
    },
    {
        "vraag": "Herleid: cos(a - b)",
        "antwoord": "cos(a)cos(b) + sin(a)sin(b)",
        "alternatieven": ["cos·cos + sin·sin", "verschilformule cos", "cos(a - b) = cos(a)cos(b) + sin(a)sin(b)"],
        "hint": "Gebruik verschilformule voor cosinus"
    },
    {
        "vraag": "Herleid: tan(2x)",
        "antwoord": "2tan(x) / (1 - tan^2(x))",
        "alternatieven": ["2tan(x)/(1 - tan²(x))", "dubbele hoek tan", "2·tan / (1 - tan²)"],
        "hint": "Gebruik de verdubbelingsformule voor tangens"
    },
    {
        "vraag": "Herleid: sin(x)cos(x)",
        "antwoord": "1/2 sin(2x)",
        "alternatieven": ["0.5sin(2x)", "(1/2)sin(2x)", "sin(x)cos(x) = ½sin(2x)"],
        "hint": "Omvormen met verdubbelingsregel: sin(x)cos(x) = ½sin(2x)"
    },
    {
        "vraag": "Wat is de amplitude van f(x) = 3sin(x)?",
        "antwoord": "3",
        "alternatieven": ["amplitude = 3", "3 eenheden", "drie"],
        "hint": "De amplitude is de voorliggende factor van sin of cos"
    },
    {
        "vraag": "Wat is de periode van f(x) = sin(2x)?",
        "antwoord": "π",
        "alternatieven": ["pi", "periode = π", "π eenheden"],
        "hint": "Periode = 2π / frequentie → 2π / 2 = π"
    },
    {
        "vraag": "Welke transformatie heeft f(x) = sin(x - π/2)?",
        "antwoord": "π/2 naar rechts",
        "alternatieven": ["verschuiving naar rechts", "horizontaal +π/2", "π/2 rechts"],
        "hint": "x - π/2 betekent horizontale verschuiving naar rechts"
    },
    {
        "vraag": "Teken de grafiek van f(x) = -2cos(x)",
        "antwoord": "Amplitude 2, gespiegeld in x-as",
        "alternatieven": ["omgekeerde cosinus", "spiegeling + amplitude 2", "-cos met 2x zo hoog"],
        "hint": "Negatief voor cos → spiegeling in x-as"
    },
    {
        "vraag": "Wat is de evenwichtsstand van f(x) = 2 + sin(x)?",
        "antwoord": "2",
        "alternatieven": ["y = 2", "evenwicht = 2", "verschuiving omhoog"],
        "hint": "Constante term buiten de sinus is verticale verschuiving"
    },
    {
        "vraag": "Stel de formule op: sinusoïde met amplitude 4, evenwichtsstand -1, periode 2π",
        "antwoord": "f(x) = 4sin(x) - 1",
        "alternatieven": ["4sin(x) - 1", "sinus met A=4 en D=-1", "y = 4sin(x) - 1"],
        "hint": "f(x) = A sin(Bx + C) + D met D = -1"
    },
    {
        "vraag": "Heeft f(x) = cos(x) lijnsymmetrie?",
        "antwoord": "Ja, lijnsymmetrie in y-as",
        "alternatieven": ["symmetrisch in y-as", "cos is even functie", "ja"],
        "hint": "cos(x) = cos(-x) → symmetrisch om de y-as"
    },
    {
        "vraag": "Heeft f(x) = sin(x) puntsymmetrie?",
        "antwoord": "Ja, om oorsprong",
        "alternatieven": ["symmetrisch in oorsprong", "ja", "sin is oneven functie"],
        "hint": "sin(-x) = -sin(x) → symmetrie in oorsprong"
    },
    {
        "vraag": "Wat is de maximale waarde van f(x) = 2sin(x) + 3?",
        "antwoord": "5",
        "alternatieven": ["max = 5", "top = 5", "2 + 3 = 5"],
        "hint": "Amplitude 2 + evenwichtsstand 3 = 5"
    },
    {
        "vraag": "Hoeveel keerpunten heeft sin(x) op [0, 2π]?",
        "antwoord": "2",
        "alternatieven": ["twee", "maximum en minimum", "2 keerpunten"],
        "hint": "sin(x) heeft één top en één dal per periode"
    },
     {
        "vraag": "Wat is de bewegingsvergelijking bij een eenparige cirkelbeweging met straal r en snelheid ω?",
        "antwoord": "x(t) = r cos(ωt), y(t) = r sin(ωt)",
        "alternatieven": ["x = r cos(ωt), y = r sin(ωt)", "x = rcos, y = rsin", "cos/sin cirkelbeweging"],
        "hint": "Gebruik parametervoorstelling van de cirkel"
    },
    {
        "vraag": "Wat stelt de functie x(t) = 5cos(2t) voor in beweging?",
        "antwoord": "Beweging met amplitude 5 en frequentie 2",
        "alternatieven": ["amplitude 5, ω = 2", "frequentie 2, max 5", "oscillatie met cos"],
        "hint": "cos-functie betekent periodieke horizontale beweging"
    },
    {
        "vraag": "Wat is de frequentie van x(t) = 3sin(4t)?",
        "antwoord": "2/π",
        "alternatieven": ["≈ 0.6366", "frequentie = 2/π", "B = 4 → f = 4 / 2π = 2/π"],
        "hint": "f = B / 2π bij sinusoïde: sin(Bt)"
    },
    {
        "vraag": "Hoe vind je de hoek waaronder een cirkelbaan een lijn snijdt?",
        "antwoord": "Gebruik de afgeleide als helling",
        "alternatieven": ["hoek = tan⁻¹(f')", "helling via afgeleide", "raaklijn gebruiken"],
        "hint": "De afgeleide geeft de richting → tan⁻¹(f’)"
    },
    {
        "vraag": "Hoe herken je een rotatie in een sinusoïde zoals x(t) = cos(t), y(t) = sin(t)?",
        "antwoord": "Het punt draait met constante snelheid in een cirkel",
        "alternatieven": ["cirkelbeweging", "eenparige rotatie", "beweging in een cirkel"],
        "hint": "cos/sin-parametrisatie geeft rotatie op een cirkel"
    },
    {
        "vraag": "Wat is de baan van het punt met x(t) = rcos(ωt), y(t) = rsin(ωt)?",
        "antwoord": "Een cirkel met straal r",
        "alternatieven": ["straal r", "ronde baan", "x² + y² = r²"],
        "hint": "cos² + sin² = 1 → x² + y² = r²"
    },
    {
        "vraag": "Hoe zie je uit een vergelijking of een rotatie linksom of rechtsom is?",
        "antwoord": "Teken de beweging of kijk naar het teken van ω",
        "alternatieven": ["ω > 0 = tegen de klok in", "positieve ω is linksom", "richting via ω"],
        "hint": "ω > 0 = tegen de klok in, ω < 0 = met de klok mee"
    },
    {
        "vraag": "Hoe kun je de richting van rotatie berekenen bij x(t) = sin(t), y(t) = cos(t)?",
        "antwoord": "Beweging is rechtsom",
        "alternatieven": ["rechtsom", "negatieve richting", "cos voor y = rechtsom"],
        "hint": "Normaal: x = cos, y = sin is linksom → omgedraaid = rechtsom"
    },
    {
        "vraag": "Wat gebeurt er met de baan bij x(t) = cos(2t), y(t) = sin(2t)?",
        "antwoord": "De rotatie is tweemaal zo snel",
        "alternatieven": ["snellere rotatie", "verdubbelde snelheid", "ω = 2 → dubbele frequentie"],
        "hint": "ω bepaalt de snelheid van draaien"
    },
    {
        "vraag": "Wat is de straal als x(t) = 6cos(t), y(t) = 6sin(t)?",
        "antwoord": "6",
        "alternatieven": ["straal = 6", "r = 6", "x² + y² = 36 → r = √36 = 6"],
        "hint": "√(x² + y²) = r"
    }

]
