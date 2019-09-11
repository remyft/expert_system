/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strclr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rfontain <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/04/04 22:49:01 by rfontain          #+#    #+#             */
/*   Updated: 2018/04/04 22:49:14 by rfontain         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>

void	ft_strclr(char *str)
{
	int i;

	if (str == NULL)
		return ;
	i = 0;
	while (str[i])
		str[i++] = '\0';
}
