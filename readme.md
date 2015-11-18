# psql_to_csv

when you forget to properly format the results of a query that takes forever


## Check it out

```
psql=> select some, stuff, and, things
psql-> from some_great_table sgt
psql-> join other_awesome_table oat on sgt.id = oat.foreign_id
psql-> where oat.some_stuff is true
some | stuff | and | things
-----+-------+-----+-------
 1   | 1     | 2   | 3
 5   | 8     | 13  | 21
 34  | 55    | 89  | 144
(3 rows)
 ```

Shit. I totally forgot to format this or write it into a file.

![facepalm](assets/facepalm.jpg)

Whelp, this format sucks, and that took like 2 hours to run! I can't copy and paste it into a spreadsheet or anything.

`psql_to_csv` to the rescue. Just copy that shit.

```
$ pbpaste | psql_to_csv | pbcopy
```

And now, in your clipboard, you've got:

```
some	stuff	and	things
1	1	2	3
5	8	13	21
34	55	89	144
```

![yey](assets/yey.jpg)

Or write it to files.

```
psql_to_csv -i psql_output.txt -o somestuffandthings.csv
```

Want a comma delimiter instead of tabs, no problem dude!

![yougotit](assets/yougotit.gif)

```
psql_to_csv -i psql_output.txt -o somestuffandthings.csv -d ','
```

## Install

```
pip install psql_to_csv
```

![thumbsup](assets/thumbsup.jpg)
