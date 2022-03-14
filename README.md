# Mince

Aktuální kurzy měn

Student: Martin Vodráška, AIK2, (https://vosplzen.cz)
License: GPL (https://www.gnu.org/licenses/gpl-3.0.html)

## Program Mince

Moje představa byla, že tento program bude zjišťovat aktulání kurz každých 5 minut z nějakého zdroje a bude ho nějak vypisovat. Toto bohužel musím přehodnotit, neboť sice existují služby, které toto umožňují, ale jsou bohužel placené. Viz třeba tento článek  (https://www.howtopython.org/4-best-python-currency-apis-for-developers/)

### K dispozici jsou tyto služby zdarma:

**fixer.io**
Free plan - aktualizace dat každou hodinu (vždy v celou)
100 API požadavků / měsíčně ... v průměru zhruba 1 požadavek za 8 hodin (3 požadavky za den)

**currencylayer.com**
Free plan - aktualizace dat jednou za den (nevím přesně kdy ⁕)
250 API požadavků / měsíčně ... v průměru zhruba 1 požadavek za 3 hodiny (8 požadavků za den)

**exchangerate-api.com**
Free plan - aktualizace dat jednou za den (nevím přesně kdy ⁕)
1500 API požadavků / měsíčně ... v průměru zhruba 1 požadavek za 30 minut (48 požadavků za den)

⁕ na webech to bohužel uvedené není, vybral jsem si jen omezený výčet převážně evropských měn, můj předpoklad tedy je, že aktualizace denního kurzu vychází z ECB kolem 16 hodiny v pracovním dnu.

V programu tedy zkusím zkombinovat výše uvedené služby a při použití free plánů hlídat jednotlivé požadavky. Z výše uvedených služeb je jasné, že vhodné pro aktuální kurzy je fixer.io, neboť ten jediný aktualizuje data každou hodinu ve free plánu. ~~Zbývající služby currencylayer.com a exchangerate-api.com lze využít pro historická data v omezené míře pouze pro denní průměry. Pro historická data použiji tedy exchangerate-api.com, má k dispozici více požadavků.~~ Knihovna forex_python nabízí aktuální denní kurz a historická data bez omezení.

Aktualizace kurzů měn je tedy možná v průměru jednou za 8 hodin (3 za den). Kombinovat je bohužel nelze, neboť z fixer.io jsou hodnoty hodinových průměrů a u ostatních dvou to jsou denní průměry. Je možné program z efektivnit a aktualizovat jen v pracovní dny kdy se s měnami obchoduje. Tím se počet požadavků zvýší na 4 za pracovní den.

Musím tedy určit tři (čtyři) časy aktualizací za všední den (možná uživatelská variabilita):

09:00, 13:30, 16:30, (20:00)

Proto musí mít program synchronizovaný přesný čas

Pro jednotlivé časy aktualizací program bude stahovat data sety pro všechny měny, které jsem v programu určil.

### Určené fiat měny:

Euro *EUR*
Americký dolar *USD*
Česká koruna *CZK*
Libra šterlinků *GBP*
Švýcarský frank *CHF*
Polský zlotý *PLN*
Ruský rubl *RUB*

### Knihovna forex_python

Tato knihovna bere denni kurzy z (https://theforexapi.com/). Toto API je cituji z dokumentace:
> Forex API je bezplatná služba pro aktuální a historické kurzy cizích měn vytvořená na základě dat zveřejňovaných Evropskou centrální bankou.

Zdá se, že tato služba je bez omezení. Historická data jsou od nyní až do 4.1. 1999
