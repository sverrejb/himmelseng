if (Verses.find().count() === 0) {
    Verses.insert({
        title: 'Vers 1',
        text: 'jeg møtte på en homofil\n ' +
        'han ville ta meg bakfra\n ' +
        'men jeg tok å lurte han\n ' +
        'jeg snudde meg og gapa'
    });

    Verses.insert({
        title: 'Vers 2',
        text: 'jeg møtte på en lommemann\n ' +
        'han hadde no i lomma\n ' +
        'det var ikke sukkertøy\n ' +
        'jeg klemte til, det skumma'
    });

    Verses.insert({
        title: 'Vers 3',
        text: 'jeg ble nå med ei kjerring hjem\n ' +
        'hun sa hun hadde mensen\n ' +
        'det burde ikke vært så galt\n ' +
        'men flomma jo som Themsen'
    });
}