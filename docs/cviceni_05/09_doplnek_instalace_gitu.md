# CVIČENÍ 5: PRÁCE SE SOUBORY, POWERSHELL A GIT

Algoritmizace a programování

## DOPLNĚK: INSTALACE GITU (JEN PRO DOMÁCÍ POČÍTAČ)

Na školních počítačích je Git už připravený.  
Tenhle doplněk potřebuješ hlavně doma.

### 1) Ověř, jestli už Git máš

```powershell
git --version
```

Když příkaz nefunguje, použij jednu z variant níže.

### 2) Instalace přes instalační soubor

1. Otevři [git-scm.com/download/win](https://git-scm.com/download/win)
2. Stáhni a spusť instalátor.
3. Pokud si nejsi jistý volbami, nech výchozí nastavení.

### 3) Instalace přes příkazovou řádku

=== "Windows (winget)"
    Základní příkaz:

    ```powershell
    winget install --id Git.Git -e --source winget
    ```

    Při instalaci se může objevit potvrzení podmínek/zdrojů (typicky `Y`) a případně UAC dialog.

    Varianta s automatickým potvrzením:

    ```powershell
    winget install --id Git.Git -e --source winget --accept-source-agreements --accept-package-agreements --silent
    ```

=== "macOS (Homebrew)"
    Pokud máš Homebrew, instalace je:

    ```bash
    brew install git
    ```

    Když `brew` nemáš, nainstaluj ho podle: [brew.sh](https://brew.sh/)

### 4) Minimální nastavení Gitu (jméno + email)

Tohle nastav i když už Git máš nainstalovaný:

```powershell
git config --global user.name "Tvoje Jmeno"
git config --global user.email "tvuj@email.cz"
```

Kontrola nastavení:

```powershell
git config --global --list
```

### 5) Pokračování

[Zpět na CÍL 4: Git a GitHub Classroom](05_cíl_4_git_a_github_classroom.md)
