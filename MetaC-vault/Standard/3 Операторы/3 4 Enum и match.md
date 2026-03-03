
Можно определить несколько вариантов на одно действие.
`case 0,2,3 => ...`
### Пример с больше меньше
```
let const x = input!(int);

match(x)
{
	< 0 => println!("Меньше нуля");
	0 => println!("Ноль");
	> 0 => println!("Больше");
}
```


### Пример с диапазоном
"Правильный вариант"
```
let const x = input!(int);

match(x)
{
	fn::lam {in [-10..0]} => println!("1");
	fn::lam {==0} => println!("2");
	fn::lam {in [0..=10] or in [20..30]} => println!("3");
	default => println!("4");
}
```
[[4 7 Лямбды]]
Сокращённый вариант.
```
let const x = input!(int);

match(x)
{
	[-10..0] => println!("1");
	0 => println!("2");
	[0..10], [20..30) => println!("3");
	default => println!("4");
}
```
Диапазоны [[2 7 Диапазоны]]

| -10 | 1   |
| --- | --- |
| -5  | 1   |
| 0   | 2   |
| 5   | 3   |
| 10  | 2   |
| 20  | 3   |
| 30  | 4   |

### Пример с перечислением
```
enum TypesOfConnection
{
	TCP,
	UDP,
	HTTP,
	SSH
}

int const t = TypesOfConnection::TCP;

match(t)
{
	TCP => print("Tcp");
	UDP => print("Udp");
	HTTP => print("Http");
	SSH => {connectSsh(); print("Ssh");}
	default => assert::raise_error();
}
```