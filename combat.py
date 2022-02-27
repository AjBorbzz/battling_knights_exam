class Combat:

    @staticmethod
    def attack(attacker, defendant):
        attack_score= attacker.base_attack + 0.5
        defend_score = defendant.base_defense

        if attacker.equipped:
            attack_score += attacker.equipped.attack

        if defendant.equipped:
            defend_score+= defendant.equipped.defense

        return (
            (attacker, defendant)
            if attack_score > defend_score else
             (defendant, attacker)
            )

    @staticmethod
    def kill_knight(knight, status=1):
        loot = knight.equipped
        last_position = knight.position

        knight.update_status(status)
        knight.position=None
        knight.equipped =None
        knight.base_attack= 0
        knight.base_defense=0

        return loot, last_position