vragenlijst = [
    {
        "vraag": "Bereken exact de schuine zijde in een rechthoekige driehoek met zijden 9 en 12.",
        "antwoord": "√225",
        "alternatieven": ["√(9² + 12²)", "√(81 + 144)", "15"],
        "hint": "c² = a² + b² = 81 + 144 = 225 → √225"
    },
    {
        "vraag": "Gebruik de sinusregel: a = 7, ∠A = 30°, ∠B = 45°. Geef b exact.",
        "antwoord": "7·sin(45°)/sin(30°)",
        "alternatieven": ["(7√2)/1", "7√2", "ongeveer 9.9"],
        "hint": "b = a·sin(B)/sin(A) = 7·sin(45°)/sin(30°)"
    },
    {
        "vraag": "Gebruik de cosinusregel: a = 10, b = 12, ∠C = 60°. Geef c² exact.",
        "antwoord": "100 + 144 - 120",
        "alternatieven": ["c² = 124", "c = √124", "√(10² + 12² - 2·10·12·cos(60°))"],
        "hint": "c² = a² + b² - 2ab·cos(C)"
    },
    {
        "vraag": "Bereken exact de oppervlakte van een driehoek met zijden 7 en 10 en ingesloten hoek 40°.",
        "antwoord": "(35·sin(40°))",
        "alternatieven": ["½·7·10·sin(40°)", "35sin(40°)", "exact in sinusvorm"],
        "hint": "Oppervlakte = ½ab·sin(C)"
    },
    {
        "vraag": "In een rechthoekige driehoek is ∠A = 30° en de schuine zijde is 12. Bereken de overstaande zijde exact.",
        "antwoord": "6",
        "alternatieven": ["12·sin(30°)", "½·12", "6.0"],
        "hint": "sin(30°) = over / 12 → over = 12·½ = 6"
    },
    {
        "vraag": "In een rechthoekige driehoek is ∠B = 60° en de aanliggende zijde is 5. Geef de schuine zijde exact.",
        "antwoord": "5 / cos(60°)",
        "alternatieven": ["10", "5 / 0.5", "schuine zijde = 10"],
        "hint": "cos(60°) = aanliggend / schuine → schuine = 5 / 0.5"
    },
    {
        "vraag": "Een cirkel heeft middellijn 10. Wat is de hoek tegenover de middellijn in een ingeschreven driehoek?",
        "antwoord": "90°",
        "alternatieven": ["rechte hoek", "∠ = 90°", "stelling van Thales"],
        "hint": "Stelling van Thales: hoek tegenover middellijn = 90°"
    },
    {
        "vraag": "In een 30°-60°-90° driehoek is de korte rechthoekszijde 5. Wat is de schuine zijde?",
        "antwoord": "10",
        "alternatieven": ["2·5", "schuine = 2×korte zijde", "hypotenusa = 10"],
        "hint": "Verhouding 1 : √3 : 2"
    },
    {
        "vraag": "Bereken exact de oppervlakte van een rechthoekige driehoek met zijden 6 en 8.",
        "antwoord": "24",
        "alternatieven": ["½·6·8", "oppervlakte = 24", "6×8÷2"],
        "hint": "½ × basis × hoogte = ½ × 6 × 8"
    },
    {
        "vraag": "In een 45°-45°-90° driehoek is de schuine zijde 10. Bereken exact de rechthoekszijde.",
        "antwoord": "10 / √2",
        "alternatieven": ["5√2", "rechthoekszijde = 10 / √2", "≈ 7.07"],
        "hint": "Verhouding 1 : 1 : √2 → rechthoekszijde = hypotenusa / √2"
    },
    
    {
        "vraag": "Bereken exact de afstand tussen de punten A(1, 2) en B(4, 6).",
        "antwoord": "√25",
        "alternatieven": ["√((4-1)² + (6-2)²)", "√(9 + 16)", "5"],
        "hint": "Gebruik de afstandsformule: √((x₂ - x₁)² + (y₂ - y₁)²)"
    },
    {
        "vraag": "Wat is de formule voor de afstand tussen punt P(x₀, y₀) en lijn ax + by + c = 0?",
        "antwoord": "|ax₀ + by₀ + c| / √(a² + b²)",
        "alternatieven": ["afstand = |ax + by + c| / √(a² + b²)", "afstandspuntenformule"],
        "hint": "Gebruik afstandsformule voor punt-lijn"
    },
    {
        "vraag": "Wat is de richtingscoëfficiënt van een lijn loodrecht op y = 2x + 1?",
        "antwoord": "-1/2",
        "alternatieven": ["negatief omgekeerd", "loodrechte helling", "m = -1/2"],
        "hint": "Vermenigvuldig hellingen: m₁·m₂ = -1"
    },
    {
        "vraag": "Wat is de richtingscoëfficiënt van een lijn loodrecht op y = -3x + 4?",
        "antwoord": "1/3",
        "alternatieven": ["m = 1/3", "reciproque positief", "helling = 1/3"],
        "hint": "Vermenigvuldig hellingen: -3 · m = -1 → m = 1/3"
    },
    {
        "vraag": "Wat is de formule van de middelloodlijn van het lijnstuk tussen A(0, 0) en B(4, 0)?",
        "antwoord": "x = 2",
        "alternatieven": ["verticale lijn bij x = 2", "loodlijn door midden", "rechte lijn x = 2"],
        "hint": "Halvering op x = 2, loodrecht = verticale lijn"
    },
    {
        "vraag": "Wat is de bissectrice van de hoeken tussen y = x en y = -x?",
        "antwoord": "y = 0",
        "alternatieven": ["x-as", "y = 0", "horizontale lijn"],
        "hint": "Hoeken zijn symmetrisch, de bissectrice is de x-as"
    },
    {
        "vraag": "Bereken de hoek tussen de lijnen y = x en y = √3 x.",
        "antwoord": "30°",
        "alternatieven": ["π/6", "hoek = 30 graden", "α = 30°"],
        "hint": "Gebruik tan(α) = |(m₂ - m₁)/(1 + m₁·m₂)| → tan(α) = √3 - 1 / (1 + √3)"
    },
    {
        "vraag": "Wat is de hoek tussen y = 2x en y = -1/2x?",
        "antwoord": "90°",
        "alternatieven": ["rechte hoek", "loodrecht", "α = 90°"],
        "hint": "Product van richtingen is -1 → hoeken staan loodrecht"
    },
    {
        "vraag": "Hoe bepaal je de hoek tussen twee krommen f(x) en g(x) in hun snijpunt?",
        "antwoord": "Gebruik afgeleiden: tan(α) = |(f'(x₀) - g'(x₀)) / (1 + f'(x₀)g'(x₀))|",
        "alternatieven": ["tan(hoek) = verschil richtingen / 1 + product", "hoek tussen raaklijnen"],
        "hint": "Hoek tussen krommen = hoek tussen raaklijnen"
    },
    {
        "vraag": "Wat is de afstand tussen het punt P(3, 4) en de lijn y = 0?",
        "antwoord": "4",
        "alternatieven": ["afstand = 4", "y-coördinaat", "afstand tot x-as = y"],
        "hint": "P ligt verticaal boven de x-as"
    },
    {
        "vraag": "Wat is de standaardvorm van de vergelijking van een cirkel met middelpunt (2, -3) en straal 5?",
        "antwoord": "(x - 2)^2 + (y + 3)^2 = 25",
        "alternatieven": ["(x - 2)² + (y + 3)² = 25", "centrum (2, -3), straal 5"],
        "hint": "Gebruik: (x - h)² + (y - k)² = r²"
    },
    {
        "vraag": "Herschrijf: x² + y² + 4x - 6y + 9 = 0 in standaardvorm.",
        "antwoord": "(x + 2)^2 + (y - 3)^2 = 4",
        "alternatieven": ["volledige kwadraatvorm", "centrum (-2, 3), straal 2"],
        "hint": "Compleet kwadraat voor x en y"
    },
    {
        "vraag": "Wat is het middelpunt en de straal van de cirkel: x² + y² - 6x + 8y + 1 = 0?",
        "antwoord": "Middelpunt (3, -4), straal 2",
        "alternatieven": ["(x - 3)² + (y + 4)² = 4", "r = 2, centrum (3, -4)"],
        "hint": "Voltooi het kwadraat voor x en y"
    },

    # 2. Cirkels die raken aan de x-as
    {
        "vraag": "Wat is de vergelijking van een cirkel met middelpunt (3, 4) die raakt aan de x-as?",
        "antwoord": "(x - 3)^2 + (y - 4)^2 = 16",
        "alternatieven": ["r = 4", "vergelijking met r = y"] ,
        "hint": "Straal = afstand van middelpunt tot x-as"
    },
    {
        "vraag": "Wat is de vergelijking van een cirkel met middelpunt (-2, r) die raakt aan de x-as?",
        "antwoord": "(x + 2)^2 + (y - r)^2 = r^2",
        "alternatieven": ["centrum (-2, r)", "y = r"],
        "hint": "Straal = y-coördinaat van het middelpunt"
    },
    {
        "vraag": "Voor welke waarden van a ligt de cirkel (x - 1)^2 + (y - a)^2 = a^2 boven de x-as?",
        "antwoord": "a > 0",
        "alternatieven": ["a positief", "y-coördinaat > 0"],
        "hint": "Voor rakende cirkels aan de x-as geldt: y = r → a > 0"
    },

    # 3. Twee snijdende cirkels
    {
        "vraag": "Wanneer snijden twee cirkels elkaar?",
        "antwoord": "Als |r1 - r2| < afstand < r1 + r2",
        "alternatieven": ["tussen verschil en som van de stralen"],
        "hint": "Gebruik driehoeksongelijkheid voor stralen en afstand"
    },
    {
        "vraag": "Snijden de cirkels met vergelijking (x - 2)^2 + y^2 = 9 en x^2 + y^2 = 4 elkaar?",
        "antwoord": "Ja",
        "alternatieven": ["afstand = 2, som = 5, verschil = 1 → 1 < 2 < 5"],
        "hint": "Bereken afstand tussen middelpunten en vergelijk met stralen"
    },
    {
        "vraag": "Kunnen twee cirkels elkaar snijden als de afstand tussen de middelpunten groter is dan de som van de stralen?",
        "antwoord": "Nee",
        "alternatieven": ["afstand > som stralen → geen snijpunten"],
    "hint": "Dan liggen ze uit elkaar"
},
{
    "vraag": "Wat is de vergelijking van de raaklijn aan de cirkel x² + y² = 25 in het punt (3, 4)?",
        "antwoord": "3x + 4y = 25",
        "alternatieven": ["raaklijnformule op punt (3,4)", "ax + by = r²"],
        "hint": "Gebruik: xx₀ + yy₀ = r² bij raakpunt (x₀, y₀)"
    },
    {
        "vraag": "Wat is de helling van de raaklijn aan de cirkel (x - 1)^2 + (y - 2)^2 = 4 in punt (3, 2)?",
        "antwoord": "0",
        "alternatieven": ["horizontaal", "raaklijn evenwijdig met x-as"],
        "hint": "(3,2) ligt op zelfde hoogte als middelpunt → y = constant"
    },

    # 5. Raaklijnen aan een cirkel zonder gegeven raakpunt
    {
        "vraag": "Hoeveel raaklijnen zijn er vanuit punt P buiten de cirkel?",
        "antwoord": "2",
        "alternatieven": ["altijd twee als P buiten ligt"],
        "hint": "Vanuit een punt buiten de cirkel zijn er twee raaklijnen"
    },
    {
        "vraag": "Gegeven de cirkel x² + y² = 16 en punt P(0, 5), wat is de afstand van P tot het middelpunt?",
        "antwoord": "√41",
        "alternatieven": ["√(0² + 5²) = √25", "√(5² + 0²)"],
        "hint": "Gebruik afstandsformule tussen (0, 0) en (0, 5)"
    },
    {
        "vraag": "Gegeven twee snijdende cirkels, hoeveel gemeenschappelijke raaklijnen hebben ze maximaal?",
        "antwoord": "2",
        "alternatieven": ["twee buitenraaklijnen"],
        "hint": "Er kunnen alleen twee raaklijnen buitenom getekend worden bij snijdende cirkels"
    },

    # 6. Vergelijkingen bij rakende cirkels
    {
        "vraag": "Wanneer raken twee cirkels elkaar uitwendig?",
        "antwoord": "Als afstand tussen de middelpunten gelijk is aan de som van de stralen",
        "alternatieven": ["d = r₁ + r₂"],
        "hint": "Uiterste punt-contact"
    },
    {
        "vraag": "Wanneer raken twee cirkels elkaar inwendig?",
        "antwoord": "Als afstand tussen de middelpunten gelijk is aan het verschil van de stralen",
        "alternatieven": ["d = |r₁ - r₂|"],
        "hint": "De ene cirkel raakt van binnen"
    },

    # 7. De ligging van een lijn t.o.v. een cirkel
    {
        "vraag": "Hoe bepaal je of een lijn de cirkel snijdt, raakt of buiten ligt?",
        "antwoord": "Vergelijk de afstand van de lijn tot het middelpunt met de straal",
        "alternatieven": ["afstand < r → snijdt", "afstand = r → raakt", "afstand > r → geen snijpunten"],
        "hint": "Gebruik afstand punt-lijn t.o.v. straal"
    },
    {
        "vraag": "Gegeven cirkel (x - 2)² + (y + 1)² = 25 en lijn y = 2x + 3. Ligt de lijn binnen, buiten of snijdend?",
        "antwoord": "Snijdend",
        "alternatieven": ["twee snijpunten", "afstand < 5"],
        "hint": "Bereken afstand van middelpunt tot de lijn en vergelijk met r"
    },

    # 8. Afstand van een punt tot een cirkel
    {
        "vraag": "Wat is de afstand van punt P(5, 0) tot de cirkel x² + y² = 9?",
        "antwoord": "√25 - 3",
        "alternatieven": ["afstand van P tot centrum is 5, straal = 3, verschil = 2"],
        "hint": "Afstand = |OP| - r"
    },
    {
        "vraag": "Wat is de afstand van punt (1,1) tot cirkel (x - 2)^2 + (y - 2)^2 = 2?",
        "antwoord": "√2 - √2",
        "alternatieven": ["0", "ligt op de cirkel"],
        "hint": "Afstand punt tot middelpunt is gelijk aan straal"
    },

    # 9. Afstand tussen twee cirkels
    {
        "vraag": "Wat is de afstand tussen twee cirkels met middelpunt (0, 0), r = 2 en (5, 0), r = 1?",
        "antwoord": "5 - 2 - 1 = 2",
        "alternatieven": ["afstand tussen centra - r₁ - r₂"],
        "hint": "Buitenste afstand = d - r₁ - r₂"
    },
    {
        "vraag": "Wat is de afstand tussen cirkels met gelijke centra en r₁ = 3, r₂ = 1?",
        "antwoord": "2",
        "alternatieven": ["3 - 1 = 2"],
        "hint": "Concentrisch: afstand = verschil van stralen"
    },

    # 10. Snijpunt van een vectorvoorstelling en een cirkel
    {
        "vraag": "Snijdt de vector r(t) = (t, t) de cirkel x² + y² = 8?",
        "antwoord": "Ja, voor t² + t² = 8 → t = ±2",
        "alternatieven": ["2t² = 8 → t² = 4", "t = ±2"],
        "hint": "Vervang x en y door t in de vergelijking"
    },
    {
        "vraag": "Snijdt r(t) = (1 + t, 2t) de cirkel (x - 1)² + y² = 1?",
        "antwoord": "Ja, voor t = ±1/√5",
        "alternatieven": ["t = ±1/√5", "t² = 1/5"],
        "hint": "Vul r(t) in de cirkelvergelijking"
    },
    {
        "vraag": "Wat is de lengte van vector v = (3, 4)?",
        "antwoord": "√25",
        "alternatieven": ["5", "√(3² + 4²)", "lengte = 5"],
        "hint": "Gebruik de formule √(x² + y²)"
    },
    {
        "vraag": "Wat is het tegengestelde van vector v = (2, -1)?",
        "antwoord": "(-2, 1)",
        "alternatieven": ["-v", "richting omgekeerd"],
        "hint": "Keer beide componenten om"
    },

    # 2. Vectoren optellen en aftrekken
    {
        "vraag": "Bereken v + w als v = (1, 2) en w = (3, -1)",
        "antwoord": "(4, 1)",
        "alternatieven": ["componentgewijs", "1+3, 2+(-1)"],
        "hint": "Tel x- en y-componenten apart op"
    },
    {
        "vraag": "Wat is v - w als v = (5, 4) en w = (2, 1)?",
        "antwoord": "(3, 3)",
        "alternatieven": ["componentgewijs verschil"],
        "hint": "Trek x- en y-componenten af"
    },

    # 3. Vectorvoorstelling
    {
        "vraag": "Wat is de vectorvoorstelling van een lijn door A(1, 2) met richtingvector (3, 1)?",
        "antwoord": "r(t) = (1 + 3t, 2 + t)",
        "alternatieven": ["(1, 2) + t·(3, 1)", "beginpunt + t·richting"],
        "hint": "Gebruik: r(t) = A + t·v"
    },
    {
        "vraag": "Wat is de vectorvoorstelling van de x-as?",
        "antwoord": "r(t) = (t, 0)",
        "alternatieven": ["richting (1, 0)", "y = 0"],
        "hint": "Alle punten met y = 0"
    },

    # 4. Inproduct
    {
        "vraag": "Bereken het inproduct van v = (1, 2) en w = (3, 4)",
        "antwoord": "11",
        "alternatieven": ["1·3 + 2·4", "dotproduct = 11"],
        "hint": "x₁·x₂ + y₁·y₂"
    },
    {
        "vraag": "Wanneer is het inproduct van twee vectoren nul?",
        "antwoord": "Als ze loodrecht op elkaar staan",
        "alternatieven": ["orthogonaal", "hoek = 90°"],
        "hint": "Inproduct = 0 bij loodrechte vectoren"
    },

    # 5. Hoek tussen twee vectoren
    {
        "vraag": "Bereken cos(θ) tussen v = (1, 0) en w = (1, 1)",
        "antwoord": "1 / √2",
        "alternatieven": ["≈ 0.707", "cos(45°)", "inproduct / (|v||w|)"],
        "hint": "Gebruik: cos(θ) = v·w / |v||w|"
    },
    {
        "vraag": "Wat is de hoek tussen v = (0, 1) en w = (1, 0)?",
        "antwoord": "90°",
        "alternatieven": ["π/2", "orthogonaal"],
        "hint": "Loodrechte vectoren"
    },

    # 6. Hoek tussen twee lijnen m.b.v. vectoren
    {
        "vraag": "Bereken de hoek tussen lijnen met richtingvectoren (1, 2) en (2, -1)",
        "antwoord": "90°",
        "alternatieven": ["inproduct = 0", "orthogonaal"],
        "hint": "Hoek via inproduct: 0 = orthogonaal"
    },
    {
        "vraag": "Wat is de hoek tussen vectoren (1, √3) en (1, -√3)?",
        "antwoord": "60°",
        "alternatieven": ["π/3", "cos(θ) = -1/2"],
        "hint": "Gebruik inproductformule voor hoek"
    },

    # 7. Normaalvector
    {
        "vraag": "Wat is een normaalvector op (3, 4)?",
        "antwoord": "(-4, 3)",
        "alternatieven": ["loodrechte vector", "(4, -3) ook juist"],
        "hint": "Wissel coördinaten en teken één om"
    },
    {
        "vraag": "Wat is een normaalvector op (1, 0)?",
        "antwoord": "(0, 1)",
        "alternatieven": ["loodrechte richting", "y-richting"],
        "hint": "Normaal op x-richting is y-richting"
    },

    # 8. Rotaties met vectoren
    {
        "vraag": "Wat is de vector (0, 1) geroteerd 90° linksom?",
        "antwoord": "(-1, 0)",
        "alternatieven": ["90° links → draai tegen de klok in"],
        "hint": "Roteer: (x, y) → (-y, x)"
    },
    {
        "vraag": "Wat is de vector (1, 0) geroteerd 90° rechtsom?",
        "antwoord": "(0, -1)",
        "alternatieven": ["rechtsom: (x, y) → (y, -x)"],
        "hint": "Roteer met de klok mee"
    },

    # 9. Zwaartepunten tekenen
    {
        "vraag": "Wat is het zwaartepunt van driehoek met hoekpunten A(0, 0), B(3, 0), C(0, 3)?",
        "antwoord": "(1, 1)",
        "alternatieven": ["gemiddelde van coördinaten", "(0+3+0)/3, (0+0+3)/3"],
        "hint": "Zwaartepunt = gemiddelde van de coördinaten"
    },
    {
        "vraag": "Wat is het zwaartepunt van A(2, 2), B(4, 0), C(0, 0)?",
        "antwoord": "(2, 2/3)",
        "alternatieven": ["(2, 0.666...)", "gemiddelde van (2,2), (4,0), (0,0)"],
        "hint": "Zwaartepunt: ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3)"
    },
    {
        "vraag": "Wanneer zijn twee raaklijnen aan een baan evenwijdig?",
        "antwoord": "Als hun richtingsvectoren gelijk zijn",
        "alternatieven": ["zelfde afgeleide", "gelijke helling"],
        "hint": "Evenwijdig = gelijke richting (zelfde afgeleide vector)"
    },
    {
        "vraag": "Voor welke t zijn de raaklijnen aan r(t) = (cos(t), sin(t)) evenwijdig?",
        "antwoord": "Voor t en t + π",
        "alternatieven": ["raakt tegen overliggend punt", "richting = tegengesteld"],
        "hint": "sinus/cosinus is periodiek"
    },

    # 2. Baansnelheid
    {
        "vraag": "Wat is de snelheid van r(t) = (3t, 4t)?",
        "antwoord": "5",
        "alternatieven": ["√(3² + 4²)", "constante snelheid 5"],
        "hint": "Snelheid is de norm van de afgeleide vector"
    },
    {
        "vraag": "Bereken de baansnelheid van r(t) = (t, t^2) op t = 1",
        "antwoord": "√5",
        "alternatieven": ["√(1² + 2²)", "snelheid = √(dx² + dy²)"],
        "hint": "Afgeleide = (1, 2) → norm = √5"
    },

    # 3. Baanversnelling
    {
        "vraag": "Wat is de versnelling van r(t) = (t, t^2)?",
        "antwoord": "(0, 2)",
        "alternatieven": ["tweede afgeleide", "versnelling = afgeleide van snelheid"],
        "hint": "Versnelling is de tweede afgeleide van de baan"
    },
    {
        "vraag": "Wat is de versnelling van r(t) = (cos(t), sin(t))?",
        "antwoord": "(-cos(t), -sin(t))",
        "alternatieven": ["negatief van r(t)", "versnelling is tegengesteld aan positievector"],
        "hint": "Tweede afgeleide van sin/cos is -sin/-cos"
    },

    # 4. De hoek waaronder de baan zichzelf snijdt
    {
        "vraag": "Wat doe je als je de hoek zoekt waaronder een baan zichzelf snijdt?",
        "antwoord": "Bepaal raaklijnen op beide snijpunten en bereken de hoek tussen die vectoren",
        "alternatieven": ["hoek tussen raakvectoren", "vergelijk afgeleiden op snijmomenten"],
        "hint": "Gebruik inproductformule tussen raakvectoren"
    },
    {
        "vraag": "r(t) = (cos(t), sin(2t)). Voor welke t snijdt de baan zichzelf?",
        "antwoord": "t en t + π",
        "alternatieven": ["periodieke eigenschappen sinus en cosinus"],
        "hint": "Kijk naar t waar r(t₁) = r(t₂) maar t₁ ≠ t₂"
    },

    # 5. Toepassingen
    {
        "vraag": "Een raket volgt r(t) = (t, t²). Wat is de richting van de snelheid op t = 2?",
        "antwoord": "(1, 4)",
        "alternatieven": ["dx/dt = 1, dy/dt = 2t = 4"],
        "hint": "Afgeleide vector op t = 2"
    },
    {
        "vraag": "Een auto beweegt volgens r(t) = (t^2, t^3). Wat is zijn versnelling op t = 1?",
        "antwoord": "(2, 6)",
        "alternatieven": ["(2t, 6t) bij t = 1"],
        "hint": "Versnelling = tweede afgeleide van r(t)"
    }

]
