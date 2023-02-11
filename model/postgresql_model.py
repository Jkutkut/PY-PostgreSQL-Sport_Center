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
    '''
    Base class for all the models that will be stored in a PostgreSQL DB.
    '''

    @classmethod
    def TABLE_NAME(cls) -> str:
        '''
        Returns the name of the table that will be used to store the model.
        '''
        return f"public.{cls.__TABLE_NAME__}"
