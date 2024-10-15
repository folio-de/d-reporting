Abfragen schreiben
=============
Dieses Dokument beschreibt Techniken für das Erstellen, Verstehen,
und Überarbeiten von LDP-basierten Abfragen.


SQL Style
---------

* Abstände/Einrückungen
	* vier Leerzeichen für Einzüge

   ```
   Beispiele einschließen

   ```

   * wenn mehr als 3 Elemente aufgelistet werden, wird jedes 
     in eine neue Zeile gesetzt
     (einschließlich des ersten)

   ```
   SELECT 
       sp.name AS service_point_name,
       m.name AS material_type,
       i.barcode AS item_barcode,
       ...
   ```

   * alternativ: das erste Elemente in derselben wird in der
     Zeile belassen, die übrigen Elemente werden an der Stelle des 
     ersten Elements eingerückt

   ```
   SELECT sp.name AS service_point_name,
          m.name AS material_type,
          i.barcode AS item_barcode,
          ...
   ```
   
   * gibt es parallele Ausdrücke, können gleiche Abstände 
     verwendet werden, um ähnliche Elemente auszurichten

   ```
   loan_date BETWEEN (SELECT start_date FROM parameters) AND
                     (SELECT end_date FROM parameters)
   ```

* Schlüsselwörter
	* in Großbuchstaben schreiben, z.B.:
		* `SELECT`
		* `'2019-01-01' :: DATE`
	* immer `AS` für Aliasing verwenden (Spalten, Unterabfragen, 
	  Tabellen, etc.)
* Leerzeilen
	* Keine Leerzeilen verwenden
* Zeichensetzung
	* `,` Am Ende einer Zeile
	* `(` Am Ende einer Zeile
	* `)` am Anfang einer Zeile, aufgereiht mit Schlüsselwort aus
          einer Zeile mit (
* Typkonvertierung
	* nutze immer `' :: '` gefolgt vom Datentyo in Großbuchstaben
	  (z.B., `VARCHAR`, `DATE`)
* Kommentare
	* `/* ... */` für mehrzeilige Kommentare
	* `--` für einzeilige Kommentare
* Dateiname
	* nutze Unterstriche, keine Bindestrichen
* Felder auswählen / selecting 
	* Nutze kein `SELECT *`. Führe alle Felder explizit auf. 
	* (join kann sich auf die gesamte Tabelle beziehen, es werden
	  keine Unterabfragen benötigt, um die richtige Tabelle mit join
	  einzuschränken) 

Strukturierung einer Abfrage
-------------------

1. Kopfzeile
	* Letztes Änderungsdatum? Aktuell ab?
	* Angeforderte Felder im Output, in der gewünschten Reihenfolge
	* Gibt es Filter?
	* Aggregiert oder nicht? (Wie?)
	* Gibt es weiteren notwendigen Kontext, um die Abfrage zu verstehen?
	* Warnung, falls die Abfrage mehr als 1 Million Zeilen (Excel) ergeben könnte?
	* Nutze diese Kopfzeile als Vorlage in der Dokumentation.
2. Parameter (`WITH` Statements verwenden)
	* Parameter am Anfang der Datei platzieren, um es anderen zu erleichtern, 
	  sie zu ändern
	* Den Name immer als "Parameter" verwenden
	* Verwendung von Parameterfeldnamen vermeiden, die zu Dubletten von LDP-Feldnamen
	  führen, wenn möglich
	* Standardparameterwerte so festlegen, dass garantiert wird, dass die Abfrage 
	  garantiert Ergebnisse bringt, sowohl für Tests als auch zur Bestätigung der 
	  Benutzer, die die Abfrage machen
		* Wenn nach einem Datumsbereich gefiltert wird, einen sehr großen
		  Standarddatumsbereich (über 10 Jahre) verwenden, auch wenn diese 
		  Abfrage typischerweise für ein einzelnes Jahr verwendet wird
		* Wenn nach einem Wert in einem bestimmten Feld gefiltert wird 
		  (z. B. einem bestimmten Servicepunkt), in Betracht ziehen, den
		  häufigsten Wert zu verwenden
3. Zusätzliche `WITH`-Statements zur Kennzeichnung von Unterabfragen (siehe z.B.
   services\_usage Abfrage) - optional
4. Hauptabfrage


Details zu spezifischen Strategien
------------------------------

* `WITH`-Statements
	* `WITH` kann genutzt werden, um zu Beginn der Abfrage temporäre Tabellen 
	  zu erstellen, die dann später verwendet werden können. 
	* Die letzte `WITH`-Anweisung geht direkt in die primäre `SELECT`-
	  Anweisung für die Abfrage. Es wird kein Komma nach dem letzten
	  `WITH`-Statement benötigt. 
	* In `WITH`-Anweisungen können Spaltennamen vor der `SELECT`-
	  Anweisung angegeben werden. Der Code ist besser lesbar, wenn
	  die Spalten mit `AS` angegeben werden, anstatt direkt im `SELECT`-
	  Statement (siehe services\_usage query)
	* [Artikel zu SQL mit WITH-Anweisungen]
	  (https://modern-sql.com/feature/with)
	* [Verwendung von WITH-Statements zur Erstellung von Literate
	  SQL](https://modern-sql.com/use-case/literate-sql)
* Abfangen von Leerstrings und Nullwerten
	* Wenn nur eine Spalte ausgewählt wird, die einen Nullwert haben 
	  könnte, muss nicht besonders vorgegangen werden. 
	* Wenn die Spalte in irgendeiner Weise umgewandelt wird, z.B. in 
	  einer mathematischen Berechnung oder wenn ein Tel des Wertes
	  extrahiert wird, muss auf einen Nullwert oder eine leere 
	  Zeichenkette getestet werden
	* Eine Möglichkeit ist die Nutzung von `COALESCE`, mit der ein 
	  Standardwert angegeben werden kann, wenn das Ergebnis null ist
* Auswahl der Tabelle, aus der zuerst ausgewählt werden soll 
	* Beim Schreiben einer Abfrage ist es wichtig, dass im Voraus 
	  überlegt wird, wechel Tabelle mit `SELECT` zuerst aufgelistet 
	  wird, da die Verknüpfungen mit `JOIN` darauf aufbauen 
	* Es sollte mit der Tabelle gestartet werden, die am besten 
	  repräsentiert, was in den Zeilen in der Ergebnistabelle ausgegeben
 	  werden soll 
		* Wenn eine Tabelle der Ausleihen ausgegeben werden soll, 
	  	  sollte mit der Ausleihtabelle gestartet werden
* `LEFT JOIN` vs. `INNER JOIN`
	*  Im Allgemeinen stellt die Verwendung von `LEFT JOIN` sicher,
	  dass Elemente nicht aus Versehen verloren werden, die am 
	  interessantesten sind
		* Wenn z.B. Interesse an den Ausleihen besteht und auch die
		  demographischen Daten der Nutzer, die die Ausleihen getätigt 
	  	  haben, angezeigt werden sollen, kann `LEFT JOIN` genutzt werden
		  um alle Ausleihen anzuzeigen, auch wenn die demographischen 
		  Angaben der Nutzer nicht bekannt sind
	* Wenn eine Tabelle auf Grundlage eines Feldes in einer sekundären Tabelle
	  gefiltert wird, sollte stattdessen ÌNNER JOIN` verwendet werden, um 
	  sicherzustellen, dass Datensätze ausgeschlossen werden, die nicht den
	  den erforderlichen Wert beinhalten
* `BETWEEN`
	* Wichtig: Die Verwendung von `BETWEEN` ist riskant für Datumsangaben, 
	  da nur Datensätze bis Mitternacht des Enddatums eingeschlossen werden
	  (Im Wesentlichen das Ende des Vortags, aber es werden auch Elemente
	  genau um Mitternacht des Enddatums mit eingeschlossen)
	* Wenn `BETWEEN` verwendet wird, sollten andere in den Kommentaren über 
	  das Verhalten bei Datumsangaben aufgeklärt werden. Zudem sollten
	  Standardwerte gesetzt werden, die für das Verhalten sinnvoll sind 
	  (z.B., der erste Tag eines Jahres und der erste Tag des folgenden 
	  Jahres, anstatt der letzte Tag des Jahres)
	* Wenn nicht riskiert werden soll, dass Werte ab Mitternacht des Enddatums 
	  einbezogen werden, kann `>= start_date` and `< end_date` anstatt von
	  `BETWEEN` gentutzt werden. Dies entspricht der Verwendung von `BETWEEN` 
	  mit dem Unterschied, dass `<` anstelle von `<=` verwendet wird. Dabei 
	  muss immer noch ein Enddatum genommen werden, das nicht in den Datumsbereich
	  eingezogen wird (der Tag nach dem letzten Tag, den eingeschlossen werden soll)
	* [Stapelabfrage zwischen Datumsbereichen]
	  (https://stackoverflow.com/questions/23335970/postgresql-query-between-date-ranges)
* DRY - Don't Repeat Yourself (Wiederholen Sie sich nicht) 
	* Wie bei jeder Programmierung gilt: Je mehr Wiederholungen es in einer 
	  Abfrage gibt, desto wahrscheinlicher ist es, dass beim Aktualisieren
	  etwas vergessen wird oder ein Fehler zum zweiten Mahl gemacht wird
	* Es sollten Wege gefunden werden, Teile von Abfragen kreativ 
	  wiederzuverwenden, entweder mit Parametern oder mit `WITH`-Statements 


Anpassung an Redshift
----------------------

* Allgemeine Hinweise
	* Das FOLIO-Reporting unterstützt LDP-basierte Abfragen sowohl auf
	  PostgreSQL als auch auf Redshift, daher müssen die Abfragen auch auf 
	  beiden laufen.
	* Der SQL-Dialekt von Redshift basiert weitgehend auf einer alten Version 
	  von PostgreSQL, aber es gibt Unterschiede. Das bedeutet, dass nicht alles, 
	  was auf PostgreSQL läuft, auch auf Redshift läuft (und umgekehrt)
* JSON-Funktionen
	* PostgreSQL hat einen sehr viel besseren JSON-Support als Redshift.
	  Redshift fast nur `json_extract_path_text()` verwenden
	* [Redshift JSON functions]
	  (https://docs.aws.amazon.com/redshift/latest/dg/json-functions.html)
* Explizite Umwandlung
	* Für alles in einer Abfrage, das nicht aus einer Datenbanktabelle stammt, 
	  müssen der Wert ausdrücklich an einen Datentyp angegeben werden (oder 
	  "umgewandelt"/"gecastet")
		* Beispiel: Alles in der temporären Tabelle der Parameter benötigt 
	  	  eine explizite Typumwandlung.
		* Beispiel: Wenn ein ad-hoc-Feld mit einem statischen Wert in der 
		  Tabelle eingefügt wird (siehe services-usage), muss der statische 
		  Wert eine explizite Typumwandlung erhalten
* Andere Probleme
	* es gab Schwierigkeiten mit den date_part-Funktionen und die Redshift-
	  Dokumentation war nicht hilfreich;  es hat eine Menge Ausprobieren 
	  und Fehlerbehebung gekostet, um das richtige Muster herauszufinden (siehe
	  services\_usage query)


