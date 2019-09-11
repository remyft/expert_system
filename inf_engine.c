/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   test.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rfontain <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/09/10 18:13:40 by rfontain          #+#    #+#             */
/*   Updated: 2019/09/10 19:05:42 by rfontain         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft/include/libft.h"


typedef enum	e_sep
{
	AND	= 1 << 0,
	OR	= 1 << 1,
	XOR	= 1 << 2
}				t_sep;

typedef struct	s_lst
{
	struct s_block	*elem;
	int				isneg;
	int				sep;
	int				*state;
	struct s_list	*next;
	struct s_list	*prev;

}				t_lst;

typedef	struct	s_block
{
	char			name;
	int				state;
	struct s_block	*side;
	t_lst			*rule;
	t_lst			*imp;
}				t_block;

int		main(void)
{
	t_block *blockA;
	t_block *blockB;
	t_block *blockC;
	t_block *blockD;
	char	*rule = "A+B=>C";

	blockA = ft_memalloc(sizeof(t_block));
	blockA->name = 'A';
	blockB = ft_memalloc(sizeof(t_block));
	blockB->name = 'B';
	blockC = ft_memalloc(sizeof(t_block));
	blockC->name = 'C';
	blockD = ft_memalloc(sizeof(t_block));
	blockD->name = 'D';
	blockC->rule = ft_memalloc(sizeof(t_lst));
	blockC->rule->elem = blockA;
	blockC->rule->state = &blockC->state;
	return (0);
}
