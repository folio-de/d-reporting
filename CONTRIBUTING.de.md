Beitrag leisten
--------------------

Wir freuen uns jederzeit über Einreichungen von Beiträgen für neue Statistikabfragen. Soweit es zeitlich möglich ist, werden alle Einreichungen berücksichtigt. Bitte haben Sie Geduld, es kann einige Zeit dauern, bis entschieden wird, ob ein Pull Request angenommen wird.

Befolgen Sie bitte diese Richtlinien, wenn Sie einen Pull Request erstellen.

##### Inhalt
1\. [Neue Beitragende](#1-Neue-Beitragende)  
2\. [Beitrag erstellen](#2-Beitrag-erstellen)  
2.1\. [Commits und Pull Requests](#21-Commits-und-Pull-Requests)  
2.2\. [Dokumentation](#22-Dokumentation)  
2.3\. [Testen](#23-Testen)  
2.4\. [SQL formatieren](#24-SQL-formatieren)  
2.5\. [Dinge benennen](#25-Dinge-benennen)  
3\. [Code Review](#3-Code-Review)  
4\. [Changelog](#4-Changelog)

1\. Neue Beitragende
--------------------

Bevor Sie mit der Erstellung eines Beitrags beginnen, empfehlen wir Ihnen, diesen im Vorfeld mit der Community zu besprechen. Dadurch haben Sie die Möglichkeit, Feedback zu erhalten, das Ihnen Zeit sparen kann. Bitte nutzen Sie hierfür den Slack Channel #d-reporting von FOLIO. 

Fehlerhinweise oder spezifische technische Vorschläge können Sie unter [Issues](https://github.com/folio-de/d-reporting/issues) einbringen.


2\. Beitrag erstellen
-----------------------------


2.1\. Commits und Pull Requests
-----------------------------

**1. Fork erstellen**

Alle Commits sollten nicht in diesem Repository, sondern in einem "forked" Repository vorgenommen werden.

**2. Branching**

Es ist eindringlich empfohlen zunächst einen neuen Unterbereich (branch) zum Hauptbereich (main) im "forked" Repository zu erstellen, sodass Commits nicht direkt im Hauptbereich (main) durchgeführt werden. Das heißt, es soll nach Möglichkeit für jeden Beitrag ein eigener Branch erstellt werden.

Pull Requests werden zusammengeführt (merge). Daher sollte der Unterbereich (branch) für die Pull Requests nach dem Zusammenführen (merge) gelöscht oder nicht wiederverwendet werden, um Verwechslung zu vermeiden. Wenn der Hauptbereich (main) für Pull Requests verwendet wird, sollte das Repository nach der Zusammenführung (merge) "re-forked" werden. 

**3. Pull Request**

Da der gesamte Pull Request in einem einzigen Commit zusammengefasst wird, ist es ratsam, den Umfang des Pull Requests einzugrenzen und vorzugsweise nur ein einzigen Beitrag abzubilden. Nutzen Sie daher bitte separate Branches.

Laut dem Git Referenzhandbuch (git reference manual) werden Git commits mit einem kurzen, einzeiligen Titel dokumentiert, der die Änderungen zusammenfasst. Darauf folgt eine ausführliche Beschreibung. Der Titel sollte nicht länger als 75 Zeichen sein. Es ist wichtig, dass der Titel aussagekräftige ist, sodass der Verlauf in Git lesbar ist. Hyperlinks oder andere Verweise wie "Fixes #" können in der ausführlichen Beschreibung enthalten sein, sollten aber nicht im Titel stehen und sollten kein Ersatz für eine vollständige Beschreibung der Änderung sein. 


2.2\. Dokumentation
-----------------

Jede Abfrage benötigt eine Benutzerdokumentation. Die Benutzerdokumentation sollte folgende drei Bereiche enthalten: 

* Zweck
* Beispiel für die Ausgabe 
* Anweisungen zur Abfrage, z.B. wie man Parameter einstellt

Bei Ergänzungen oder Änderungen von Abfragen sollten die entsprechenden Ergänzungen oder Änderungen auch in der Benutzerdokumentation ergänzt werden, und zwar im selben Pull Request.


2.3\. Testen
-----------

Alle Abfragen oder Änderungen an Abfragen sollten getestet werden, bevor sie in einem Pull Request eingefügt werden. Wir verfügen nicht über Testdaten, die umfangreiche automatisierte Tests ermöglichen.


2.4\. SQL formatieren
------------------

Um ein einheitliches Erscheinungsbild bei SQL-Abfragen zu haben, gibt es Formatierungsregeln. Diese Formatierungsregeln befinden sich unter QUERIES.md im Repository.


2.5\. Dinge benennen
-----------------

Die Namen von Tabellen und Spalten sind in Kleinbuchstaben zu schreiben und durch Unterstriche ( `_` ) zu trennen. Doppelte Unterstriche ( `__` ) sollten vermieden werden, da sie zum Beispiel in der Metadb als spezielle Indikatoren verwendet werden.

In dem seltenen Fall, dass ein Spaltenname sowohl mit einem reservierten Wort identisch ist als auch ohne Tabellen- oder Alias-Präfix allein steht, muss er in Anführungszeichen ( `"` ) gesetzt werden. Davon abgesehen ist es besser, keine Anführungszeichen zu verwenden. 


3\. Code Review
---------------

Ein Pull Request wird von mindestens einer anderen Personen als dem Beitragenden geprüft, bevor er mit dem Repository zusammengeführt (merge) werden kann.

Wenn ein Prüfer vorschlägt, die Änderungen um zusätzliche Funktionen zu erweitern, müssen diese Änderungen nicht im aktuellen Pull Request behandelt werden, sondern können in einem separaten, neuen Pull Request behandelt werden.

Die unten aufgeführte Checkliste kann als Leitfaden für die eigene Überprüfung (Review) eines Pull Requests (PR) verwendet werden. Eine Kopie der Liste kann als Kommentar an einem Review beigefügt werden. Kreuzen Sie dazu die Punkte in der Checkliste an, die in Ihrer Überprüfung (Review) bestätigt wurden, indem Sie in jeder Zeile ein `x` zwischen den eckigen Klammern `[]` setzen.

Wenn einige Punkte nicht angekreuzt sind oder Sie weitere Fragen haben, können Sie dies ebenfalls in einem Kommentar angeben und "Request changes" (Änderungen beantragen) bei der Überprüfung wählen.

```
- [ ] Titel und Beschreibung des PR sind präzise und vollständig
- [ ] PR ist in einem neuen Branch (nicht main)
- [ ] PR ist nicht zu umfangreich
- [ ] Die Abfrage läuft ohne Fehler
- [ ] Die Ausgabe der Abfrage ist korrekt
- [ ] Die Abfragelogik ist klar und gut dokumentiert
- [ ] Die Abfrage ist lesbar und richtig eingerückt (Formatierungsregeln)
- [ ] Tabellen- und Spaltennamen werden in Kleinbuchstaben geschrieben
- [ ] Anführungszeichen werden nur verwendet, wenn dies erforderlich ist
- [ ] Die Abfrage hat eine vollständige Benutzerdokumentation
    - [ ] Zweck
    - [ ] Beispiel für die Ausgabe
    - [ ] Anweisungen zur Abfrage, z.B. wie man Parameter einstellt
```


4\. Changelog
-----------------------------

Die Datei CHANGES.md wird als Changelog verwendet. Mit jedem Release werden die Release notes aktualisiert, welche die in den Pull Requests vorgenommenen Änderungen beschreiben. Dabei handelt es sich um eine in sich eigenständige, textliche Zusammenfassung der Änderungen und nicht um Verlinkungen.