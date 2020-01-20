#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    def __init__(self, pos):
        self.x, self.y = pos
        
    def __add__(self, obj):
        """возвращает сумму двух векторов"""
        return Vec2d((self.x + obj.x, self.y + obj.y))
    
    def __sub__(self, obj):
        """"возвращает разность двух векторов"""
        return Vec2d((self.x - obj.x, self.y - obj.y))
            
    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        x = self.x * k
        y = self.y * k
        return Vec2d((x, y))
    
    def __len__(self):
        """возвращает длину вектора"""
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def int_pair(self):
        return int(self.x), int(self.y)
    
    def vec(self, obj):
        """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
        координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
        return __sub__(obj, self)


class Polyline:
    def sets(self, steps):
        self.steps = steps
    
    def set_points(self):        
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p] = Vec2d((- self.speeds[p].x, self.speeds[p].y))
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p] = Vec2d((self.speeds[p].x, -self.speeds[p].y))
        return self.points
        
    def draw_points(self):
        for p in self.points:
            self.game.draw.circle(self.display, (255, 255, 255),
                            p.int_pair(), self.width)

    def draw_help(self):
        """функция отрисовки экрана справки программы"""
        self.display.fill((50, 50, 50))
        font1 = self.game.font.SysFont("courier", 24)
        font2 = self.game.font.SysFont("serif", 24)
        data = []
        data.append(["F1", "Show Help"])
        data.append(["R", "Restart"])
        data.append(["P", "Pause/Play"])
        data.append(["D", "Remove last knot"])
        data.append(["Num+", "More points"])
        data.append(["Num-", "Less points"])
        data.append(["1 or 2", "Switching between curves"])
        data.append(["I", "Increas the speed of the last knot"])
        data.append(["L", "Decrease the speed of the last knot"])
        data.append(["", ""])
        data.append([str(self.steps), "Current points"])

        self.game.draw.lines(self.display, (255, 50, 50, 255), True, [
            (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            self.display.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            self.display.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))
    
    
class Knot(Polyline):    
    def __init__(self, game):
        self.game = game
        self.points = []
        self.speeds = []
        self._speed_step = 0.2

    def sets(self, display, width, color, steps):
        """устанавливает параметры кривой"""
        self.display = display
        self.width = width
        self.color = color
        super().sets(steps)
        
    def add_point(self, point, speed):
        """добавляет точку"""
        self.points.append(Vec2d(point))
        self.speeds.append(Vec2d(speed))
        
    def reset_point(self):
        """удалает все точки"""
        self.points = []
        self.speeds = []
        
    def remove_last_point(self):
        """удаляет последнюю точку"""
        self.points = self.points[:-1]
        self.speeds = self.speeds[:-1]
        
    def increas_speed_last_point(self):
        """увеличивает скорость последней точки"""
        if self.speeds:
            x = self._speed_step if self.speeds[-1].x > 0 else -self._speed_step
            y = self._speed_step if self.speeds[-1].y > 0 else -self._speed_step
            self.speeds[-1] += Vec2d((x, y))
            
    def reduction_speed_last_point(self):
        """уменьшает скорость последней точки"""
        if self.speeds:
            x, y = 0, 0
            if abs(self.speeds[-1].x) > self._speed_step:
                x = self._speed_step if self.speeds[-1].x > self._speed_step else -self._speed_step
            if abs(self.speeds[-1].y) > self._speed_step:
                y = self._speed_step if self.speeds[-1].y > self._speed_step else -self._speed_step
            self.speeds[-1] -= Vec2d((x, y))
    
    def get_knot(self):        
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append(((self.points[i] + self.points[i + 1]) * 0.5))
            ptn.append(self.points[i + 1])
            ptn.append(((self.points[i + 1] + self.points[i + 2]) * 0.5))

            res.extend(self.get_points(ptn))
        return res
    
    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return ((points[deg] * alpha) + (self.get_point(points, alpha, deg - 1) * (1 - alpha)))

    def get_points(self, base_points):
        alpha = 1 / self.steps
        res = []
        for i in range(self.steps):
            res.append(self.get_point(base_points, i * alpha))
        return res
    
    def draw(self):
        """функция отрисовки точек на экране"""
        points = self.get_knot()
        for p_n in range(-1, len(points) - 1):
            self.game.draw.line(self.display, self.color,
                            (int(points[p_n].x), int(points[p_n].y)),
                            (int(points[p_n + 1].x), int(points[p_n + 1].y)), self.width)

        super().draw_points()


def worker(game):
    gameDisplay = game.display.set_mode(SCREEN_DIM)
    steps = 35
    working = True
    show_help = False
    pause = True
    num_knot = 0

    hue = 0
    color = game.Color(0)
    knots = []
    # добавляем две кривые
    knots.append(Knot(game))
    knots.append(Knot(game))

    while working:
        for event in game.event.get():
            if event.type == game.QUIT:
                working = False
            if event.type == game.KEYDOWN:
                if event.key == game.K_ESCAPE:
                    working = False
                if event.key == game.K_r:
                    for knot in knots:
                        knot.reset_point()
                if event.key == game.K_p:
                    pause = not pause
                if event.key == game.K_d:
                    knots[num_knot].remove_last_point()
                if event.key == game.K_KP_PLUS:
                    steps += 1
                if event.key == game.K_F1:
                    show_help = not show_help
                if event.key == game.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0
                if event.key in [game.K_1, game.K_KP1]:
                    num_knot = 0
                if event.key in [game.K_2, game.K_KP2]:
                    num_knot = 1
                # регулируем скорость последнего добавленного узла
                if event.key == game.K_i:
                    knots[num_knot].increas_speed_last_point()
                if event.key == game.K_l:
                    knots[num_knot].reduction_speed_last_point()

            if event.type == game.MOUSEBUTTONDOWN:
                knots[num_knot].add_point(event.pos, (random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        
        for i in range(len(knots)):
            knots[i].sets(gameDisplay, 3, color, steps)
            knots[i].draw()            
            if not pause:
                knots[i].set_points()
        if show_help:
            knots[num_knot].draw_help()
        
            
        game.display.flip()


def main():
    pygame.init()
    pygame.display.set_caption("MyScreenSaver")

    worker(pygame)

    pygame.display.quit()
    pygame.quit()
    exit(0)
    


if __name__ == "__main__":
    main()
