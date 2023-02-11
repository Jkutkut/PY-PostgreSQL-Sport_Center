# **************************************************************************** #
#                                                                              #
#                                                         .-------------.      #
#                                                         |.-----------.|      #
#                                                         ||           ||      #
#                                                         ||  Jkutkut  ||      #
#    postgresql_model.py                                  ||           ||      #
#                                                         |'-----------'|      #
#    By: Jkutkut  https://github.com/jkutkut              /:::::::::::::\      #
#                                                        /:::::::::::::::\     #
#    Created: 2023/02/11 18:05:55 by Jkutkut            /:::===========:::\    #
#    Updated: 2023/02/11 18:05:57 by Jkutkut            '-----------------'    #
#                                                                              #
# **************************************************************************** #

class PostgreSQLModel:
    @classmethod
    def TABLE_NAME(cls) -> str:
        return f"public.{cls.__TABLE_NAME__}"
