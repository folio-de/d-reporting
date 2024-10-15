Beiträge
============

Wir freuen uns jederzeit über Einreichungen von SQL-Statements für neue 
Statistikabfragen (report queries), Abfragen für abgeleiteten Tabellen 
(derived tabeles) sowie für Fehlerbehebungen. Soweit es zeitlich möglich ist,
werden alle Einsendungen berücksichtigt. Bitte haben Sie Geduld, es kann 
einige Zeit dauern, bis entschieden wird, ob ein Pull Request angenommen wird.

Befolgen Sie bitte diese Richtlinien, wenn Sie eine Pull-Anfrage erstellen.

##### Inhalt
1\. [Neue Beitragende](#1-Neue-Beitragende)  
2\. [Commits und Pull-Anfragen](#2-Commits-und-Pull-Anfragen)  
3\. [Überprüfung des Codes](#3-Ueberpruefung-des-Codes)  
4\. [Dokumentation](#4-Dokumentation)  
5\. [Testen](#5-testen)  
6\. [Derived tables / abgeleitete Tabellen](#6-derived-tables)  
7\. [Formatierung von SQL](#7-Formatierung-von-SQL)  
8\. [Benennen](#8-Benennen)  
9\. [Checkliste](#9-Checkliste)


1\. Neue Beitragende
--------------------

Bevor Sie mit der Erstellung eines Beitrags beginnen, empfehlen wir Ihnen, 
diesen im Vorfeld mit der Community zu besprechen. Dadurch haben Sie die 
Möglichkeit, Feedback zu erhalten, das Ihnen Zeit sparen kann.

Die meisten Beitragenden nutzen hierfür den internationalen #reporting-lab 
channel in FOLIO Slack. Die deutsche Community erreichen Sie über den 
#d-reporting Channel in FOLIO Slack.

Alternativ können Sie auch gerne Fragen direkt in Github stellen. 
Allgemeine Fragen können Sie hier stellen: [Discussions]
(https://github.com/folio-org/folio-analytics/discussions)
Fehler oder spezifische technische Vorschläge können Sie hier einbringen:
[Issues](https://github.com/folio-org/folio-analytics/issues).


2\. Commits und Pull-Anfragen
-----------------------------

### Änderungen vornehmen

Alle Commits sollten nicht in diesem Repository, sonder in einem "forked" 
Repository vorgenommen werden.

Es ist **eindringlich empfohlen** zunächst einen Unterbereich zum 
"Hauptbereich" zu erstellen, sodass Commits nicht direkt im Hauptbereich 
durchgeführt werden. 

**Pull requests werden zusammengeführt. Daher sollte der Unterbereich 
für die Pull requests nach dem Zusammenführen verworfen oder nicht 
wiederverwendet werden, um Verwechslung zu vermeiden.** Wenn der 
'Hauptbereich' für Pull requests verwendet wird, sollte das Repository 
nach der Zusammenführung der Bereiche "re-forked" werden. 

Da der gesamte Pull Request in einem einzigen Commit zusammengefasst wird, 
ist es ratsam, den Umfang der Anfrage einzugrenzen und vorzugsweise nur ein 
einziges Problem abzufragen.


### Commit Beschreibung

Laut dem Git Referenzhandbuch (git reference manual) werden Git commits
mit einem kurzen, einzeiligen Titel dokumentiert, der die Änderungen 
zusammenfasst. Darauf folgt eine ausführliche Beschreibung. 
Der Titel sollte nicht länger als 75 Zeichen sein. Es ist wichtig, 
dass der Titel aussagekräftige ist, sodass der Verlauf in Git lesbar ist. 
Hyperlinks oder andere Verweise wie "Fixes #" können in der ausführlichen 
Beschreibung enthalten sein, sollten aber nicht im Titel stehen und sollten 
kein Ersatz für eine vollständige Beschreibung der Änderung sein. 


### CHANGES.md

Die Datei CHANGES.md sollte mit Releasenotes aktualisiert werden, 
die die in der Pull-Anfrage vorgenommenen Änderungen beschreiben.
Dabei sollte es sich um eine in sich eigenständige, textliche 
Zusammenfassung der Änderungen handeln und nicht um einen Link.



3\. Überprüfung des Codes (Review)
---------------

Ein Pull Request wird von mindestens zwei anderen Personen als dem 
Beitragenden geprüft, bevor er zusammengeführt werden kann.

Wenn ein Prüfer vorschlägt, die Änderungen um zusätzliche Funktionen zu 
erweitern, müssen diese Änderungen nicht im aktuellen Pull Request 
behandelt werden, sondern können in einem separaten, neuen Pull Request 
behandelt werden.

Im Folgenden finden Sie eine empfohlene Checkliste für Code Reviews.


4\. Dokumentation
-----------------

Bei Ergänzungen oder Änderungen von Abfragen sollten die entsprechenden 
Ergänzungen oder Änderungen auch in der Benutzerdokumentation ergänzt werden, 
und zwar im selben Pull Request.

Die Benutzerdokumentation sollte folgende drei Bereiche enthalten: 

* Zweck der Meldung
* Beispiel für die Ausgabe 
* Anweisungen zur Abfrage, z.B. wie man Parameter einstellt


5\. Testen
-----------

Alle Abfragen oder Änderungen an Abfragen sollten mit einer LDP-Datenbank getestet werden, 
bevor sie in einem Pull request eingefügt werden. Derzeit verfügen wir noch nicht über 
Testdaten, die umfangreiche automatisierte Tests ermöglicht.


6\. Derived tables / abgeleitete Tabellen
------------------

Bei Ergänzungen oder Änderungen an derived tables sollten die entsprechenden 
Ergänzungen oder Änderungen auch in der Datei `runlist.txt` nachvollzogen werden, 
und zwar im selben Pull Request.

Abfragen zu derived tables für Metadb sollten ebenfalls alle relevanten externen 
SQL-Direktiven enthalten, insbesondere:

```
--metadb:table <table>
```


7\. SQL formatieren
------------------

Wir nutzen das Tool `pg_format` von 
[pgFormatter](https://github.com/darold/pgFormatter), um den SQL-Code lesbarer 
zu gestalten. Um maximale Konsistenz zu gewährleisten, wurde eine [Konfigurations-Datei]
(https://github.com/folio-org/folio-analytics/blob/main/sql/pg_format.conf)
zur Verfügung gestellt. Die Konfigurations-Datei sollte als `~/.pg_format` 
kopiert werden.

Bitte verwenden Sie diese Methode zur Formatierung des vorgeschlagenen Codes.

Beachten Sie, dass `pg_format` bekannte Probleme hat, insbesondere bei 
[Formatierung CTEs](https://github.com/darold/pgFormatter/issues/213). 
In diesem Fall wird eine manuelle Formatierung bevorzugt.


8\. Dinge benennen
-----------------

Die Namen von Tabellen und Spalten sind in Kleinbuchstaben zu schreiben 
und durch Unterstriche ( `_` ) zu trennen. Doppelte Unterstriche ( `__` ) 
sollten vermieden werden, da sie in der Metadb als spezielle Indikatoren 
verwendet werden.

In dem seltenen Fall, dass ein Spaltenname sowohl mit einem reservierten Wort 
identisch ist als auch ohne Tabellen- oder Alias-Präfix allein steht, muss er 
in Anführungszeichen ( `"` ) gesetzt werden. Davon abgesehen ist es besser, 
keine Anführungszeichen zu verwenden. 

Bei derived tables folgen die Tabellennamen nicht einem rein mechanischen Muster, 
was dazu führen kann, dass einige Namen unpraktisch lang sind.
Der Schema-/Tabellenname der ersten nach `FROM` aufgeführten Tabelle wird 
normalerweise als Präfix für den abgeleiteten Tabellennamen verwendet, zum Beispiel
`instance_` or `item_`. Hinzu kommt oft ein Suffix, das auf die wichtigste 
Tabellenverbindung hinweist, oder `ext` für allgemeine Erweiterungen der Daten. 
Insgesamt ist es hilfreich, sich Gedanken darüber zu machen, wie man die 
abgeleitete Tabelle kurz und knapp beschreiben kann.


9\. Checkliste
-------------

Die unten aufgeführte Checkliste kann als Leitfaden für die eigene Überprüfung 
eines Pull Requests (PR) verwendet werden. Eine Kopie der Liste kann als Kommentar
an einem Review/einer Überprüfung beigefügt werden. Kreuzen Sie dazu die Punkte
in der Checkliste an, die in Ihrer Überprüfung bestätigt wurden, indem Sie 
in jeder Zeile ein `x` zwischen den eckigen Klammern `[]` setzen.

Wenn einige Punkte nicht angekreuzt sind oder Sie weitere Fragen haben, können Sie 
dies ebenfalls in einem Kommentar angeben und "Request changes" (Änderungen beantragen) 
bei der Überprüfung wählen.

```
Alle Abfragen:
- [ ] Titel und Beschreibung des PR sind präzise und vollständig
- [ ] PR steht in einem neuen Unterbereich (nicht im Hauptbereich)
- [ ] PR ist nicht zu umfangreich
- [ ] Die Abfrage läuft ohne Fehler
- [ ] Die Ausgabe der Abfrage ist korrekt
- [ ] Die Abfragelogik ist klar und gut dokumentiert
- [ ] Die Abfrage ist lesbar und richtig eingerückt
- [ ] Tabellen- und Spaltennamen werden in Kleinbuchstaben geschrieben
- [ ] Anführungszeichen werden nur verwendet, wenn dies erforderlich ist
- [ ] Auszug von JSON hat die Standardform, zum Beispiel:
      LDP:     t #>> '{f1,f2,f3}'    [für Kompatibilität zwischen LDP 1 & 2]
      Metadb:  jsonb_extract_path_text(t, f1, f2, f3)

Bericht zur Abfrage:
- [ ] Die Abfrage hat eine vollständige Benutzerdokumentation
    - [ ] Zweck der Meldung
    - [ ] Beispiel für die Ausgabe
    - [ ] Anweisungen zur Abfrage, z.B. wie man Parameter einstellt


Derived tables/abgeleitete Tabellen:
- [ ] Erste Zeile ist die Anweisung  "--metadb:table", gefolgt von einer Leerzeile
- [ ] Benutzerdokumentation in Kommentarzeilen, gefolgt von Leerzeilen
- [ ] Der Dateiname wird in `runlist.txt` nach den Abhängigkeiten aufgeführt
```
