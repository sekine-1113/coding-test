# coding-test

コーディングテストの練習ができます。

問題は、`problem01`, `problem02` のような形式で設定してあります。

それぞれ内容が異なっており、様々なテストを実施できます。

入力は `inputs`, 期待される出力は `tests` に格納されています。

解答は `problemXX/src/main.py` に記述してください。

新たにファイルを作ったり、外部ライブラリを使用することは可能です。

`python3 run.py` を実行すると、自動的にテストが行われ結果が表示されます。

解答する問題を変更する場合は、 `config.json` の `problem` を変更してください。

以下では、`config.json` の中身を説明します。

```json
{
    "problem": "problem01",
    "entry_point": "src/main.py",
    "inputs": "inputs",
    "outputs": "outputs",
    "tests": "tests",
    "script:run:posix": "python3 [entry_point] < [input] > [output]",
    "script:run:nt": "python [entry_point] < [input] > [output]",
    "timeout_seconds": 3
}
```

|key|value|description|
|:--|:--|:--|
|problem|problem01|解答する問題。変更可能|
|entry_point|src/main.py|実行するスクリプト|
|inputs|inputs|テストの入力用ファイルがあるディレクトリ|
|outputs|outputs|テストの出力用ファイルがあるディレクトリ|
|tests|tests|テストの期待される出力用ファイルがあるディレクトリ|
|script:run:posix|python3 [entry_point] < [input] > [output]|Linux用Python実行コマンド|
|script:run:nt|python [entry_point] < [input] > [output]|Windows用Python実行コマンド|
|timeout_seconds|5|タイムアウトの秒数|

`srcipt:run:*` では、 `[entry_point]`, `[input]`, `[output]` が利用可能です。

|key|description|
|:--|:--|
|[entry_point]|実行するスクリプト|
|[input]|入力するファイル名|
|[output]|出力するファイル名|

ここに記述されているものはすべて変更が可能です。
