//14. Даны две строки. Вычеркнуть из строки А символы, встречающиеся в строке В.
var a,b:string;
    i:byte;
begin
    write('рядок A = ');readln(a);
    write('рядок B = ');readln(b);
    for i:=Length(a) downto 1 do
      while Pos(a[i],b)>0 do
        Delete(a,i,1);
    writeln('Результат = ',a);
end.
