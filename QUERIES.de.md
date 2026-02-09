Abfragen schreiben
--------------------

Dieses Dokument beschreibt Techniken für das Erstellen, Verstehen und Überarbeiten von SQL-Abfragen.

**Inhalt**

1\. [SQL Style](#1-SQL-Style)  
1.2\. [Abstände und Einrückungen](#12-Abstaende-und-Einrueckungen)  
1.3\. [Schlüsselwörter](#13-Schluesselwoerter)  
1.4\. [Leerzeilen](#14-Leerzeilen)  
1.5\. [Typkonvertierung](#15-Typkonvertierung)  
1.6\. [Kommentare](#16-Kommentare)  
1.7\. [Dateiname](#17-Dateiname)  
2\. [Strukturierung einer Abfrage](#2-Strukturierung-einer-Abfrage)  
3\. [Spezifische Strategien](#3-Spezifische-Strategien)  
4\. [Kompatibilität Redshift](#4-Kompatibilität-Redshift) 


1\. SQL Style
--------------------


1.2\. Abstände und Einrückungen
--------------------

* Es werden 4 Leerzeichen für Einzüge verwendet.

```
SELECT 
    column
FROM
    table
```

* Jedes Elemente wird in eine neue Zeile gesetzt.

```
SELECT 
    sp.name AS service_point_name,
    m.name AS material_type,
    i.barcode AS item_barcode,
    ...
```

* Gibt es parallele Ausdrücke, können gleiche Abstände verwendet werden, um ähnliche Elemente auszurichten.

```
    loan_date BETWEEN (SELECT start_date FROM parameters) AND
                      (SELECT end_date FROM parameters) 
```


1.3\. Schlüsselwörter
--------------------

Schlüsselwörter sind in Großbuchstaben zu schreiben, z.B.:

* `SELECT`
* `'2019-01-01' :: DATE`
* Immer `AS` für Aliasing verwenden (Spalten, Unterabfragen, Tabellen, etc.)


1.4\. Leerzeilen
--------------------

Es werden keine Leerzeilen verwendet.


1.5\. Typkonvertierung
--------------------

Sollte eine Typkonvertierung notwendig sein, wird immer `' :: '` gefolgt vom Datentyp in Großbuchstaben genutzt, z.B. `VARCHAR` oder `DATE`.


1.6\. Kommentare
--------------------

* `/* ... */` für mehrzeilige Kommentare
* `--` für einzeilige Kommentare


1.7\. Dateiname
--------------------

Es werden zur Abgrenzung Unterstriche verwendet, keine Bindestriche.


2\. Strukturierung einer Abfrage
--------------------

1. Kopfzeile

Bitte folgenden Kopf zu jeder Abfrage hinzufügen und die folgenden Punkte anpassen.

* File name
* Author
* Description

Wenn eine Abfrage abgewandelt weiterverwendet wird, so wird unter `Author` noch `Modification` ergänzt mit den eigenen persönlichen Angaben.

```
/*
-------------------------------------------------------------------------------
File name

Author:         John Doe <jd@example.org>
Description:    Brief description of the purpose.
-------------------------------------------------------------------------------
Copyright 2026 The Open Library Foundation

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-------------------------------------------------------------------------------
*/
```

2. Warnungen zur Performance
    
Schreiben Sie eine Warnung in `Description`, falls die Abfrage mehr als 1 Million Zeilen (Excel) ergeben könnte oder die Verarbeitung sehr viele Ressourcen benötigt.

3. Parameter 
    
* Parameter werden innerhalb einer CTE definiert (`WITH` Statements verwenden).
* Parameter am Anfang der Datei platzieren, um es anderen zu erleichtern, sie zu ändern.
* Standardparameterwerte so festlegen, dass garantiert wird, dass die Abfrage garantiert Ergebnisse bringt. Gegebenenfalls müssen Standardwerte oder ein logisches ODER (z.B. mit 1=1) verwendet werden.

4. Unterabfragen werden als zusätzliche `WITH`-Statements erstellt.

5. Hauptabfrage


3\. Spezifische Strategien
------------------------------

* Abfangen von Leerstrings und Nullwerten
    * Wenn **nur eine Spalte** ausgewählt wird, die einen NULL-Wert haben könnte, muss nicht besonders vorgegangen werden. 
	* Wenn die Spalte in irgendeiner Weise umgewandelt wird, z.B. in einer mathematischen Berechnung oder wenn ein Teil des Wertes extrahiert wird, muss auf einen NULL-Wert oder eine leere Zeichenkette getestet werden. Eine Möglichkeit ist die Nutzung von `COALESCE`, mit der ein Standardwert angegeben werden kann, wenn das Ergebnis NULL ist.
* Auswahl der Tabelle, aus der zuerst ausgewählt werden soll 
	* Beim Schreiben einer Abfrage ist es wichtig, dass im Voraus überlegt wird, welche Tabelle mit `SELECT` zuerst aufgelistet wird, da die Verknüpfungen mit `JOIN` darauf aufbauen.
	* Es sollte mit der Tabelle gestartet werden, die am besten repräsentiert, was in den Zeilen in der Ergebnistabelle ausgegeben werden soll. Das steigert die Performance.
* `LEFT JOIN` vs. `INNER JOIN`
    * Im Allgemeinen stellt die Verwendung von `LEFT JOIN` sicher, dass Elemente nicht aus Versehen verloren werden, die am interessantesten sind
        * Wenn z.B. Interesse an den Ausleihen besteht und auch die demographischen Daten der Nutzer, die die Ausleihen getätigt haben, angezeigt werden sollen, kann `LEFT JOIN` genutzt werden um alle Ausleihen anzuzeigen, auch wenn die demographischen Angaben der Nutzer nicht bekannt sind.
    * Wenn eine Tabelle auf Grundlage eines Feldes in einer sekundären Tabelle gefiltert wird, sollte stattdessen ÌNNER JOIN` verwendet werden, um sicherzustellen, dass Datensätze ausgeschlossen werden, die nicht den den erforderlichen Wert beinhalten.
* `BETWEEN`
    * Wichtig: Die Verwendung von `BETWEEN` ist riskant für Datumsangaben, da nur Datensätze bis Mitternacht des Enddatums eingeschlossen werden. Im Wesentlichen das Ende des Vortags, aber es werden auch Elemente genau um Mitternacht des Enddatums mit eingeschlossen.
    * Wenn `BETWEEN` verwendet wird, sollten andere in den Kommentaren über das Verhalten bei Datumsangaben aufgeklärt werden. Zudem sollten Standardwerte gesetzt werden, die für das Verhalten sinnvoll sind (z.B., der erste Tag eines Jahres und der erste Tag des folgenden Jahres, anstatt der letzte Tag des Jahres).
    * Wenn nicht riskiert werden soll, dass Werte ab Mitternacht des Enddatums einbezogen werden, kann `>= start_date` and `< end_date` anstatt von `BETWEEN` gentutzt werden. Dies entspricht der Verwendung von `BETWEEN` mit dem Unterschied, dass `<` anstelle von `<=` verwendet wird. Dabei muss immer noch ein Enddatum genommen werden, das nicht in den Datumsbereich eingezogen wird (der Tag nach dem letzten Tag, den eingeschlossen werden soll)
* DRY - Don't Repeat Yourself (Wiederholen Sie sich nicht) 
    * Wie bei jeder Programmierung gilt: Je mehr Wiederholungen es in einer Abfrage gibt, desto wahrscheinlicher ist es, dass beim Aktualisieren etwas vergessen wird oder ein Fehler zum zweiten Mal gemacht wird.
    * Es sollten Wege gefunden werden, Teile von Abfragen kreativ wiederzuverwenden, entweder mit Parametern oder mit `WITH`-Statements 


4\. Kompatibilität Redshift
----------------------

* Allgemeine Hinweise
    * Das FOLIO-Reporting unterstützt Abfragen sowohl auf PostgreSQL als auch auf Redshift, daher müssen die Abfragen auch auf beiden laufen.
    * Der SQL-Dialekt von Redshift basiert weitgehend auf einer alten Version von PostgreSQL, aber es gibt Unterschiede. Das bedeutet, dass nicht alles, was auf PostgreSQL läuft, auch auf Redshift läuft (und umgekehrt).
* JSON-Funktionen
    * PostgreSQL hat einen sehr viel besseren JSON-Support als Redshift. Redshift kann fast nur `json_extract_path_text()` verwenden.
	* [Redshift JSON functions](https://docs.aws.amazon.com/redshift/latest/dg/json-functions.html)
* Type Casting (Typumwandlung)
    * Alle Werte in einer Abfrage, das nicht aus einer Datenbanktabelle stammen, müssen explizit umgewandelt / gecastet werden.
