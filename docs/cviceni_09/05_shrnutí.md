# CVIČENÍ 9: ZÁKLADY GIT A GITHUB

Algoritmizace a programování

## SHRNUTÍ

V tomto cvičení jsme se naučili:

1. **Nastavit Git**: Nakonfigurovat jméno, email a výchozí větev (`git config --global`).
2. **Založit repozitář**: Inicializovat nový repozitář příkazem `git init`.
3. **Ignorovat soubory**: Vytvořit `.gitignore` pro vyloučení nepotřebných souborů.
4. **Sledovat soubory**: Přidávat soubory ke sledování pomocí `git add`.
5. **Vytvářet revize**: Ukládat změny do historie pomocí `git commit`.
6. **Zobrazovat změny**: Používat `git status`, `git diff` a `git show` pro přehled o stavu.
7. **Procházet historii**: Využívat `git log`, `gitk` a grafické nástroje v PyCharmu.
8. **Pracovat s větvemi**: Vytvářet (`git branch`), přepínat (`git switch`) a mazat větve.
9. **Slučovat větve**: Používat `git merge` a řešit konflikty při slučování.
10. **Spolupracovat přes GitHub**: Klonovat repozitáře (`git clone`), vytvářet forky a pull requesty.
11. **Synchronizovat změny**: Nahrávat (`git push`) a stahovat (`git pull`) změny ze vzdáleného repozitáře.

---

### Tahák: nejpoužívanější příkazy

| Příkaz                                   | Co dělá                                          |
|------------------------------------------|--------------------------------------------------|
| `git config --global user.name "Jmeno"`  | Nastaví jméno autora                             |
| `git config --global user.email "email"` | Nastaví email autora                             |
| `git init`                               | Založí nový repozitář                            |
| `git status`                             | Ukáže stav souborů (co je změněné, co je staged) |
| `git add soubor`                         | Přidá soubor do stage (připraví k commitu)       |
| `git add .`                              | Přidá **všechny** změněné soubory do stage       |
| `git commit -m "popis"`                  | Vytvoří revizi s popisem                         |
| `git diff`                               | Ukáže změny oproti poslednímu commitu            |
| `git log --oneline`                      | Kompaktní historie revizí                        |
| `gitk --all`                             | Grafický prohlížeč historie                      |
| `git gui`                                | Grafické rozhraní pro add/commit/push            |
| `git show`                               | Detail poslední revize                           |
| `git branch nazev`                       | Vytvoří novou větev                              |
| `git switch nazev`                       | Přepne na větev                                  |
| `git switch -c nazev`                    | Vytvoří větev a přepne na ni                     |
| `git merge nazev`                        | Sloučí větev do aktuální                         |
| `git branch -d nazev`                    | Smaže větev                                      |
| `git clone URL`                          | Naklonuje vzdálený repozitář                     |
| `git remote -v`                          | Vypíše vzdálené repozitáře                       |
| `git push remote vetev`                  | Nahraje revize na vzdálený repozitář             |
| `git pull remote vetev`                  | Stáhne a sloučí změny ze vzdáleného repozitáře   |
