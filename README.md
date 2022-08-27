# yastyleguide
Yet another styleguide


## Install

```bash
poetry add -D yastyleguide
```

```bash
pip install yastyleguide
```

## Nitpick styleguide

You can use base settings for linters with [nitpick](https://github.com/andreoliwa/nitpick):
```toml
[tool.nitpick]
style = "https://gitlab.com/ds.team/general/yastyleguide/-/blob/master/styles/nitpick-yastyle.toml"
```
<details><summary>Публичный вариант</summary>

```toml
[tool.nitpick]
style = "https://raw.githubusercontent.com/levkovalenko/yastyleguide/master/styles/nitpick-yastyle.toml"
```
</details>

## Running
It's just plugin **flake8**, so:
```bash
flake8 .
```

## Violations
Our own codes:
|Code|Description|
|----|-----------|
|YASG101|`Don't use any 'for' loops.`|
|YASG102|`Don't use any 'while' loops.`|
|YASG201|`Line is to complex, {0} > {1}. To many ast nodes per line.`|
|YASG202|`To big median line complexity in module, {0} > {1}.`|
|YASG203|`To many lines per module, {0} > {1}.`|
|YASG204|`To many function definitions per module, {0} > {1}.`|
|YASG205|`To many class definitions per module, {0} > {1}.`|

You can read about external plugins violations at [/docs/eng/plugin_list.md](docs/eng/plugin_list.md)