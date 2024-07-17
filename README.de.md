# d-reporting

[![en](https://img.shields.io/badge/lang-en-red.svg)](README.md)

Copyright (C) 2024 The Open Library Foundation

Diese Software wird unter den Bedingungen der Apache-Lizenz, Version 2.0, vertrieben. Weitere Informationen finden Sie in der Datei "[LICENSE](LICENSE)".

# Überblick

Dieses Repository ist eine gemeinsame Ablage der deutschen FOLIO-Gemeinschaft für das FOLIO-Reporting. Es enthält SQL-Queries für Datenbankabfragen und andere Dateien für alternative Reporting-Techniken, die für FOLIO entwickelt wurden. Der Inhalt besteht zum Großteil aus Dateien, die von der FOLIO-Reporting-Community entwickelt wurden und auf den Anforderungen der deutschen FOLIO-Gemeinschaft basieren. Der Fokus des Repositorys liegt auf der Deutschen Bibliotheksstatistik (DBS).

# Mitarbeiten

Jeder ist willkommen, Beiträge einzureichen. Wir bitten Sie, sich vorher unsere Richtlinien unter "Contributing.md" durchzulesen.

# Wie verwendet man das Repository?

Das Repository ist als eine gemeinsame Ablage von Dateien zu verstehen, die bei Bedarf verwendet werden können. In manchen Fällen können bestimmte Verzeichnisse von Programmen möglicherweise integriert werden und so eine automatisierte Nachnutzung ermöglichen. In diesen Fällen übernehmen wir gemäß der Lizenz jedoch keine Garantie oder Haftung für den ordnungsgemäßen Betrieb.

Eine ausführliche Dokumentation für die Verwendung der Dateien befindet sich im Wiki des Repositorys.

# Versionierung

## Branches

Es gibt zwei Haupttypen von Branches:

* `main` Dies ist ein Branch für die Entwicklung, in dem neue Funktionen zunächst zusammengeführt werden. Dieser Branch ist relativ instabil. Der Branch ist die Standardansicht auf GitHub.
* Release branches (`release-*`). Dies sind Releases von `main`. Sie werden als stabile Branches geführt; Das heißt, sie erhalten möglicherweise Fehlerbehebungen, aber im Allgemeinen keine neuen Funktionen. Produktive Systeme sollten einen dieser Branches benutzen.

## Releases

Releases werden als separater Branch veröffentlicht. Diese Release branches (`release-*`) sind fortlaufend nummeriert. Es gibt keine konkreten Termine, wann ein Release erscheint. Die FOLIO-Reporting-Community entscheidet gemeinsam über die Termine.