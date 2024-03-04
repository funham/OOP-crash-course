'''
A little guide on python's type annotations:

def foo(arg1: TypeOfArg1, arg2: TypeOfArg2) -> RetTypeOfFoo:
    ...  # body

'''


import db
from enum import Enum


class Engine:
    def __init__(self, name: str, horse_power: int) -> None:
        ...


class Tires:
    def __init__(self, name: str, k_friction: float) -> None:
        ...


class Car:
    '''
    The Car class uses composition for objects like name and engine
    and aggregates tires. Leaving car without tires would invalidate
    it's state and thus should be prevented.

    The philosophical difference between composition and aggregation is
    that when using composition, the bigger object (master) "owns" the smaller one (slave).
    On the other hand, when using aggregation, the master only "borrows" slave.

    With composition slave object cannot exist out of master's context, UNLESS the master
    itself lands it to some other object. This feature is poorely presented in languages
    like C# or Python, but naturally implemented in Rust or C++.
    '''

    def __init__(self, name: str, engine: Engine, tires: Tires) -> None:
        ...

    def change_compound(self, tires: Tires) -> None:
        '''
        Replaces car's old tire compound with a new one.
        '''
        ...


class Racist:

    class SkillLevel(Enum):
        '''
        Don't look at the numbers below, it's actually
        stupid python's way to implement enums.
        You'll get to it in C#. For now just focuc on
        words in CAPS. 
        '''
        AMATEUR = 1  # noob
        AVERAGE = 2  # avg-
        ADVANCED = 3  # avg
        SKILLED = 4  # avg+
        GOAT = 5  # pro

    def __init__(self, name: str, skill_lvl: SkillLevel) -> None:
        ...

    def get_skill_factor(self) -> float:
        '''
        Yields sF for calculating the formula.
        '''
        ...


class Team:
    '''
    Team is composed of blah blah blah just do your shit
    '''

    def __init__(self, name: str, driver: Racist, car: Car) -> None:
        ...

    def calculate_race_time(self) -> float:
        '''
        The method that calculates the total time of two laps of the race.
        '''
        ...


def fetch_db() -> list[Team]:
    '''
    This function creates the list of teams using data from data base
    and returns it to the caller (the code where this functon is used).

    this pattern is something similar to the `factory` but it's a story for another day ;)
    '''
    res: list[Team] = []

    for team_name in db.db_teams:
        t = Team(...)
        res.append(t)

    return res


def main() -> None:
    # 2 following lines of code are written in functional style. Feel the difference.
    teams = fetch_db()
    # use python's lambda function to do this.
    top_teams: list[str] = list(map(..., sorted(teams, key=...)))

    print('Result board:')
    for i, team_name in enumerate(top_teams):
        print(f'{i}: {team_name}')


if __name__ == '__main__':
    main()
