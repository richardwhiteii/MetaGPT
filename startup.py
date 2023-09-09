#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import platform
import fire

from metagpt.roles import Architect, Engineer, ProductManager
from metagpt.roles import ProjectManager, QaEngineer
from metagpt.software_company import SoftwareCompany


async def startup(
    idea: str,
    investment: float = 3.0,
    n_round: int = 5,
    code_review: bool = False,
    run_tests: bool = False,
    implement: bool = True
):
    """Run a startup. Be a boss."""
    company = SoftwareCompany()
    company.hire([
        ProductManager(),
        Architect(),
        ProjectManager(),
    ])

    # if implement or code_review
    if implement or code_review:
        # developing features: implement the idea
        company.hire([Engineer(n_borg=5, use_code_review=code_review)])

    if run_tests:
        # developing features: run tests on the spot and identify bugs
        # (bug fixing capability comes soon!)
        company.hire([QaEngineer()])

    company.invest(investment)
    company.start_project(idea)
    await company.run(n_round=n_round)


import os

def main(
    idea: str,
    investment: float = 3.0,
    n_round: int = 5,
    code_review: bool = True,
    run_tests: bool = False,
    implement: bool = True
):
    """
    We are a software startup comprised of AI. By investing in us,
    you are empowering a future filled with limitless possibilities.
    :param idea: Your innovative idea, such as "Creating a snake game."
    :param investment: As an investor, you have the opportunity to contribute
    a certain dollar amount to this AI company.
    :param n_round:
    :param code_review: Whether to use code review.
    :return:
    """
    # Check if the idea is a file path
    if os.path.isfile(idea):
        # If it is, read the file and use its content as the prompt_content
        with open(idea, 'r') as file:
            prompt_content = file.read()
    else:
        # If it's not a file path, use the idea as the prompt_content directly
        prompt_content = idea

    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(startup(prompt_content, investment, n_round,
                code_review, run_tests, implement))


if __name__ == '__main__':
    fire.Fire({
        'p': main,
        '--prompt': main
    })
    
