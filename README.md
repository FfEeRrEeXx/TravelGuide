# TravelGuide - Intelligenter Reiseplanungs-Assistent
Ein Chatbot für Reiseplanung mit KI-gestützter Entscheidungslogik und Tool-Calling-Integration.

- **Intelligente Entscheidungslogik**: Das System wählt automatisch die passenden Tools
- **Hotel-Suche**: Automatische Hotelsuche mit Preisvergleich
- **Wetter-Abfragen**: Aktuelle Wetterdaten für beliebige Städte
- **Attraktionen**: Sehenswürdigkeiten und Reiseempfehlungen
- **Reiseplanung**: Intelligente Reisevorschläge
- **Feedback-System**: Bewertung der Antwortqualität

## Installation

1. **Repository klonen**:
```bash
git clone <repository-url>
cd TravelGuide
```

2. **Virtuelle Umgebung erstellen**:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oder
venv\Scripts\activate     # Windows
```

3. **Abhängigkeiten installieren**:
```bash
pip install -r requirements.txt
```

4. **Umgebungsvariablen konfigurieren**:
```bash
# Bearbeiten config.env mit API-Keys
```

5. **Anwendung starten**:
```bash
python main.py
```

## Verwendung

1. Öffne `http://localhost:5001` im Browser

2. Stelle Fragen wie:
   - "Wie ist das Wetter in Wien?"
   - "Hotels in Barcelona finden"
   - "Sehenswürdigkeiten in Paris"
   - "Empfehlungen für Amsterdam"


## Print der Diagramme
python data/evaluation/balkendarstellung.py
python data/evaluation/kategorie.py
python data/evaluation/zeitlicherverlauf.py
python data/evaluation/modelPerformance.py

## API
https://openweathermap.org/api


