# Задача Коши

## Уравнение

$$ \frac{\partial^2u(x,t)}{\partial t^2} = \frac{\partial^2u(x,t)}{\partial x^2} - \sin(u(x,t)) $$

на решетке от 0 до 10 с шагом $dx = 0.005$

и начальными условиями:

- Возьмите в качестве начальных данных $u(x,t_0)$ и $u'(x,t_0)$ для $t_0$ волновой пакет перещающийся со скоростью $v$. 

- Найти $u(x,t)$ при $t = 150$.

- Подберите скорость так, чтобы пакет перемещался с одного края решетки до другого, но не выходил за пределы решетки.

- Постройте картину движения пакета.


## Зависимости

Для запуска кода вам потребуется Python с библиотеками NumPy и Matplotlib. Вы можете установить их с помощью следующих команд:

```bash
git clone https://github.com/brazenoptimist/physic_task.git
cd physic_task
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python task.py
```

## Результат

![result](gifs/wave_packet.gif)

